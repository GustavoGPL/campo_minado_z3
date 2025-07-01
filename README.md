# 🧠 Campo Minado com Inferência Lógica (Z3)

Este é um projeto de **Campo Minado com raciocínio lógico**, que utiliza o **solver Z3** para inferir automaticamente o status de células ocultas com base nas pistas reveladas.

🔎 O sistema informa se uma célula é:
- 💣 **Mina garantida**
- ✅ **Segura garantida**
- ❓ **Indeterminada**

---

## 🖥️ Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [Z3 Solver (SMT)](https://github.com/Z3Prover/z3) — desenvolvido pela Microsoft Research

---

## 📦 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/campo-minado-z3.git
cd campo-minado-z3
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv

# Ative o ambiente virtual:
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

---

- O programa revela automaticamente uma célula inicial.
- Você deve digitar as coordenadas no formato `linha,coluna` (sem espaços) para revelar novas células.

Exemplo:

```

### 🧩 Legenda do Tabuleiro

| Símbolo | Significado                         |
|---------|-------------------------------------|
| `M`     | 💣 Mina garantida (evite clicar!)   |
| `S`     | ✅ Segura garantida (pode clicar)   |
| `?`     | ❓ Indeterminado                     |
| `0-8`   | Número de minas ao redor            |

---

## 📚 Sobre a Lógica Utilizada

A cada célula revelada com um número `n`, é criada uma **restrição lógica**:

> A soma das variáveis booleanas das células vizinhas deve ser igual a `n`.

O sistema usa o Z3 para verificar se:
- A célula **tem que ser** uma mina (mina garantida)
- A célula **tem que ser** segura (segura garantida)
- Ou se ainda **é indeterminado**

---

## 🧠 Exemplo de Tabuleiro Interno

```txt
* 2 1 1
2 3 * 1
1 * 3 2
1 1 2 *
```

Minas são representadas internamente com `-1` no código.

---

## 📌 Aplicação Acadêmica

Este projeto foi desenvolvido como trabalho da disciplina **Lógica para Programação**, com os seguintes objetivos:
- Utilizar **lógica proposicional**
- Representar conhecimento com variáveis booleanas
- Aplicar **SAT solver** para inferência automática
- Demonstrar aplicação prática de raciocínio lógico

---

## 📄 Licença

Este projeto é livre para fins acadêmicos e educacionais.