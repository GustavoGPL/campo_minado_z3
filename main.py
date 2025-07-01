from z3 import Solver, Bool, Sum, If

# Função para pegar os vizinhos válidos de uma célula
def vizinhos(i, j, N, M):
    for x in range(max(0, i - 1), min(N, i + 2)):
        for y in range(max(0, j - 1), min(M, j + 2)):
            if (x, y) != (i, j):
                yield (x, y)

# Revela uma célula e atualiza o solver com as restrições
def revelar_celula(i, j, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M):
    if tabuleiro_visivel[i][j] != '.':
        return

    valor = tabuleiro_real[i][j]
    tabuleiro_visivel[i][j] = str(valor)

    solver.add(variaveis_minas[(i, j)] == False)
    soma = Sum([If(variaveis_minas[(x, y)], 1, 0) for x, y in vizinhos(i, j, N, M)])
    solver.add(soma == valor)

    if valor == 0:
        for (x, y) in vizinhos(i, j, N, M):
            revelar_celula(x, y, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)

# Consulta com o Z3 se uma célula é mina garantida, segura garantida ou indeterminada
def consultar_certeza(i, j, solver, variaveis_minas):
    from z3 import Solver as Z3Solver, sat
    var = variaveis_minas[(i, j)]

    s1 = Z3Solver()
    s1.add(solver.assertions())
    s1.add(var == True)
    pode_ser_mina = (s1.check() == sat)

    s2 = Z3Solver()
    s2.add(solver.assertions())
    s2.add(var == False)
    pode_ser_segura = (s2.check() == sat)

    if pode_ser_mina and not pode_ser_segura:
        return "mina garantida"
    elif not pode_ser_mina and pode_ser_segura:
        return "segura garantida"
    else:
        return "indeterminado"

# Exibe o tabuleiro visível com o status de células ocultas
def imprimir_tabuleiro(tabuleiro_visivel, solver, variaveis_minas, N, M):
    print("\nTabuleiro visível e status das células ocultas:")
    for i in range(N):
        linha = ""
        for j in range(M):
            c = tabuleiro_visivel[i][j]
            if c == '.':
                status = consultar_certeza(i, j, solver, variaveis_minas)
                if status == "mina garantida":
                    linha += "M "
                elif status == "segura garantida":
                    linha += "S "
                else:
                    linha += "? "
            else:
                linha += c + " "
        print(linha)
    print()

# Execução principal do jogo
def main():
    tabuleiro_real = [
        [-1, 2, 1, 1],
        [2, 3, -1, 1],
        [1, -1, 3, 2],
        [1, 1, 2, -1],
    ]

    N = len(tabuleiro_real)
    M = len(tabuleiro_real[0])
    tabuleiro_visivel = [['.' for _ in range(M)] for _ in range(N)]
    variaveis_minas = {(i, j): Bool(f"m_{i}_{j}") for i in range(N) for j in range(M)}
    solver = Solver()

    # Revelações manuais estratégicas que alimentam o Z3 com pistas suficientes
    revelar_celula(0, 1, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(0, 2, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(0, 3, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(1, 0, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(1, 1, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(1, 3, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)
    revelar_celula(2, 2, tabuleiro_real, tabuleiro_visivel, solver, variaveis_minas, N, M)

    imprimir_tabuleiro(tabuleiro_visivel, solver, variaveis_minas, N, M)

    print("Consulta para células ocultas:")
    for i in range(N):
        for j in range(M):
            if tabuleiro_visivel[i][j] == '.':
                status = consultar_certeza(i, j, solver, variaveis_minas)
                print(f"Célula ({i},{j}): {status}")

if __name__ == "__main__":
    main()
