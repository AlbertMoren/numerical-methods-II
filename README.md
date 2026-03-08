# Métodos Numéricos II
Este projeto é uma implementação em Python de diversos algoritmos abordados na disciplina de Métodos Numéricos 2. A arquitetura foi desenhada separando a lógica de negócio (Back-end) da interface de usuário (Front-end), permitindo cálculos rápidos e uma visualização amigável.

##  Tecnologias Utilizadas

* **Back-end:** [FastAPI](https://fastapi.tiangolo.com/) para criação da API RESTful e Pydantic para validação de dados.
* **Front-end:** [Streamlit](https://streamlit.io/) para a construção da interface gráfica iterativa.
* **Linguagem:** Python 3.x

##  Arquitetura do Projeto

O projeto segue o Princípio da Responsabilidade Única (SRP), isolando as rotas da API das classes matemáticas:

```text
metodos_numericos/
├── backend/
│   ├── api.py                 # Rotas e controladores da API (FastAPI)
│   ├── models.py              # Modelos de dados esperados (Pydantic)
│   └── metodos/               # Classes com a lógica matemática isolada
│       └── derivada_primeira.py
├── frontend/
│   └── app.py                 # Interface do usuário (Streamlit)
├── requirements.txt           # Dependências do projeto
└── README.md
```

## Como Executar Localmente

Para rodar o projeto na sua máquina, você precisará de dois terminais abertos executando simultaneamente (um para a API e outro para o Front-end).

1. Configuração Inicial

Clone o repositório, crie um ambiente virtual e instale as dependências:

```text
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows

# Instale as dependências
pip install -r requirements.txt
```

2. Rodando a API (Back-end)

No Terminal 1 (com o ambiente virtual ativado), inicie o servidor do FastAPI:

```text
uvicorn backend.api:app --reload
```

3. Rodando a Interface (Front-end)

No Terminal 2 (também com o ambiente virtual ativado), inicie o Streamlit:

```text
streamlit run frontend/app.py
```

### Módulo 1: Derivação Numérica
- [x] Derivada de 1ª Ordem (Métodos: Forward, Backward e Central)
- [ ] Derivada de 2ª Ordem
- [ ] Derivada de 3ª Ordem