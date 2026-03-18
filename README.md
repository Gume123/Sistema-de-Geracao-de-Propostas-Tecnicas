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

✔ Login com autenticação JWT
✔ Interface web simples para preenchimento de dados
✔ Seleção dinâmica de templates PowerPoint
✔ Substituição automática de variáveis no template
✔ Download automático do arquivo gerado
✔ Remoção automática de arquivos temporários

---

# 🧩 Tecnologias Utilizadas

### Backend

- Python
- FastAPI
- python-pptx
- Uvicorn
- JWT (python-jose)
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript (Vanilla)

### Infraestrutura

- API REST
- Autenticação stateless via JWT
- Geração dinâmica de arquivos

---

# 🏗️ Arquitetura do Sistema

O sistema segue uma arquitetura simples baseada em **API REST + Frontend estático**.

```
Frontend (HTML / JS)
        │
        ▼
FastAPI Backend
        │
        ├── Autenticação JWT
        ├── Listagem de Templates
        └── Geração de Propostas
                │
                ▼
        python-pptx
                │
                ▼
        Arquivo PowerPoint gerado
```

Fluxo principal:

1. Usuário realiza login
2. Recebe token JWT
3. Interface envia requisições autenticadas
4. Backend processa template PPTX
5. Sistema retorna o arquivo gerado

---

# 📂 Estrutura do Projeto

```
gerador-propostas/
│
├── app
│   ├── main.py
│   ├── auth.py
│   ├── models.py
│   ├── ppt_generator.py
│   └── config.py
│
├── frontend
│   ├── login.html
│   └── index.html
│
├── templates
│   └── modelos_de_proposta.pptx
│
├── temp
│   └── arquivos_gerados
│
├── docs
│   ├── login.png
│   └── interface.png
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação e Execução

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Gume123/Sistema-de-Geracao-de-Propostas-Tecnicas
```

```bash
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
pip install fastapi uvicorn python-pptx pydantic python-jose passlib[bcrypt] python-multipart
```

---

## 4️⃣ Executar o servidor

```bash
python run.py
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000/login.html
```

---

# 🔐 Autenticação

O sistema utiliza **JSON Web Token (JWT)** para autenticação.

Fluxo:

1. Usuário envia credenciais para `/login`
2. Backend retorna um token
3. Token é armazenado no `localStorage`
4. Requisições subsequentes incluem o token no header

Exemplo de header:

```
Authorization: Bearer <token>
```

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

1. O template é carregado
2. O sistema percorre slides, caixas de texto e tabelas
3. As variáveis são substituídas pelos valores do formulário

---

# 📦 Geração de Arquivos

Quando uma proposta é criada:

1️⃣ Template é carregado
2️⃣ Dados são inseridos no PPTX
3️⃣ Arquivo é salvo temporariamente
4️⃣ Arquivo é enviado para download
5️⃣ Arquivo temporário é removido automaticamente

Isso evita acúmulo de arquivos no servidor.

---

# 🧠 Decisões Técnicas

Algumas escolhas importantes no projeto:

**FastAPI**

Escolhido por oferecer:

- alta performance
- tipagem forte com Pydantic
- documentação automática
- desenvolvimento rápido

---

**python-pptx**

Permite manipular apresentações PowerPoint programaticamente:

- editar textos
- percorrer tabelas
- substituir placeholders

---

**JWT Authentication**

Escolhido por:

- evitar sessões no servidor
- simplificar deploy
- permitir integração futura com APIs

---

# 🔧 Possíveis Melhorias

- autenticação com banco de dados
- controle de usuários
- histórico de propostas geradas
- upload de templates pela interface
- exportação em PDF
- deploy em cloud (AWS / Railway / Render)
- geração automática de número de proposta

---

# 📈 Roadmap

Versões futuras planejadas:

**v1.1**

- logout
- expiração de sessão
- proteção completa das rotas frontend

**v1.2**

- sistema de usuários
- banco de dados

**v2.0**

- dashboard administrativo
- upload de templates
- geração de PDF

---

# 📜 Licença

Projeto desenvolvido para uso interno da **Só Hélices**.

Uso externo requer autorização.
