# ⚙️ Gerador de Propostas Técnicas

### Automação de propostas comerciais em PowerPoint

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Status](https://img.shields.io/badge/Status-Em%20uso-success)
![License](https://img.shields.io/badge/Licença-Interna-lightgrey)

Sistema desenvolvido para automatizar a geração de **propostas comerciais e técnicas em PowerPoint**, utilizando templates pré-configurados.

A aplicação permite que vendedores ou técnicos preencham um formulário simples e gerem automaticamente um arquivo `.pptx` com todas as informações estruturadas.

Este projeto foi criado para **uso interno da Só Hélices**, com o objetivo de reduzir o tempo de criação de propostas e padronizar documentos comerciais.

---

# 📸 Interface

### Tela de login

<img src="https://sohelices.com.br/wp-content/uploads/2026/03/Captura-de-tela-2026-03-10-135619.png" width="500">

### Gerador de proposta

<img src="https://sohelices.com.br/wp-content/uploads/2026/03/Captura-de-tela-2026-03-10-135655.png" width="700">

---

# 🚀 Principais Funcionalidades

✔ Login com autenticação JWT e Banco de Dados
✔ Sistema de cadastro e controle de usuários
✔ Interface web simples para preenchimento de dados
✔ Seleção dinâmica de templates PowerPoint
✔ Substituição automática de variáveis no template
✔ Download automático do arquivo gerado
✔ Remoção automática de arquivos temporários
✔ **Deploy automatizado na nuvem (Render)**
✔ **Banco de dados Híbrido (SQLite local / PostgreSQL produção)**

---

# 🧩 Tecnologias Utilizadas

### Backend

- Python
- FastAPI
- SQLAlchemy & PostgreSQL/SQLite (Banco de Dados)
- python-pptx
- Uvicorn
- JWT (python-jose) & Passlib (Bcrypt)
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript (Vanilla)

### Infraestrutura

- API REST
- Autenticação stateless via JWT
- Geração dinâmica de arquivos
- Deploy contínuo no **Render**

---

# 🏗️ Arquitetura do Sistema

O sistema integra o **Frontend** e a **API** em um servidor unificado, utilizando banco de dados para segurança e persistência:

```
Frontend (HTML / JS)
        │
        ▼ (Requisições Relativas)
FastAPI Backend (app.main)
        │
        ├── Autenticação JWT ◄── Banco de Dados (PostgreSQL / SQLite)
        ├── Listagem de Templates
        ├── Gerenciamento de Usuários
        └── Geração de Propostas
                │
                ▼
        python-pptx
                │
                ▼
        Arquivo PowerPoint gerado
```

---

# 📂 Estrutura do Projeto

```
gerador-propostas/
│
├── app/
│   ├── main.py          # Ponto de entrada (Backend + Frontend Estático)
│   ├── auth.py          # Lógica de login e JWT
│   ├── models.py        # Modelos do Banco de Dados
│   ├── database.py      # Conexão com SQLite / PostgreSQL
│   ├── crypt.py         # Hashes de senha
│   ├── ppt_generator.py # Substituição de variáveis no PPTX
│   └── config.py        # Variáveis de ambiente
│
├── frontend/
│   ├── index.html       # Painel Principal
│   ├── login.html       # Tela de Login
│   └── usuarios.html    # Tela de Criação de Usuários
│
├── templates/
│   └── modelos_de_proposta.pptx
│
├── temp/
│   └── (Arquivos gerados temporariamente)
│
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (Local)
└── README.md
```

---

# ⚙️ Instalação e Execução (Local)

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Gume123/Sistema-de-Geracao-de-Propostas-Tecnicas
cd gerador-propostas
```

---

## 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

---

## 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Executar o servidor

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000/
```

---

# ☁️ Deploy no Render

O projeto está configurado para deploy imediato no **Render**.

1. Crie um **Web Service** com ambiente `Python 3`.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Crie um **Banco de Dados PostgreSQL** no Render e adicione a "Internal Database URL" como a variável de ambiente `DATABASE_URL` no seu Web Service.
5. Configure as demais variáveis (`SECRET_KEY`, `USUARIO`, `SENHA`, etc.).

---

# 🔐 Autenticação e Usuários

O sistema utiliza **JSON Web Token (JWT)** e **Senhas Hashadas (Bcrypt)**.
- O primeiro usuário Admin é criado automaticamente ao iniciar o banco de dados pela primeira vez com base nas credenciais do `.env`.
- Novos usuários podem ser cadastrados via painel na rota `/usuarios.html` (apenas por usuários logados).

---

# 📄 Funcionamento dos Templates

Os templates PowerPoint devem conter **placeholders** no formato:

```
{{proposta}}
{{aleta}}
{{diametro_aleta}}
{{preco_unitario}}
{{frete_pac}}
```

Durante a geração da proposta:
1. O template é carregado da pasta `templates/`.
2. O sistema percorre slides, caixas de texto e tabelas.
3. As variáveis são substituídas pelos valores do formulário.

---

# 🔧 Possíveis Melhorias Futuras

- Histórico de propostas geradas (salvar no banco de dados)
- Upload de novos templates diretamente pela interface web
- Exportação dos arquivos em PDF
- Geração automática sequencial de número de proposta

---

# 📜 Licença

Projeto desenvolvido para uso interno da **Só Hélices**.
Uso externo requer autorização.
