from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from fastapi.responses import FileResponse
import os
import uuid
from fastapi.middleware.cors import CORSMiddleware
from .models import PropostaData
from .auth import login_usuario, usuario_logado
from .ppt_generator import preencher_pptx, remover_arquivo
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Gerador de Propostas Só Hélices")

os.makedirs("temp", exist_ok=True)

from .database import engine, Base, SessionLocal, get_db
from sqlalchemy.orm import Session
from .models import Usuario, UsuarioCreate
from .crypt import gerar_hash_senha
from .config import USUARIO, SENHA

# Criar as tabelas do banco de dados (SQLite)
Base.metadata.create_all(bind=engine)

# Criar usuario admin inicial se nao existir
db = SessionLocal()
try:
    admin = db.query(Usuario).filter(Usuario.username == USUARIO).first()
    if not admin:
        admin_user = Usuario(
            username=USUARIO,
            password_hash=gerar_hash_senha(SENHA),
            role="admin"
        )
        db.add(admin_user)
        db.commit()
finally:
    db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(data = Depends(login_usuario)):
    return data

@app.post("/usuarios")
async def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(usuario_logado) # Apenas logados podem criar
):
    db_user = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Nome de usuário já cadastrado")
        
    novo_usuario = Usuario(
        username=usuario.username,
        password_hash=gerar_hash_senha(usuario.password),
        role=usuario.role
    )
    db.add(novo_usuario)
    db.commit()
    
    return {"message": "Usuário criado com sucesso!", "username": novo_usuario.username}

@app.get("/templates")
async def listar_templates(user: str = Depends(usuario_logado)):

    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta = os.path.join(base_dir, "..", "templates")

    if not os.path.exists(pasta):
        return []

    arquivos = [
        f for f in os.listdir(pasta)
        if f.endswith(".pptx") and not f.startswith("~$")
    ]

    return arquivos

@app.post("/gerar-proposta")
async def gerar_proposta(
    dados: PropostaData,
    template_nome: str,
    background_tasks: BackgroundTasks,
    user: str = Depends(usuario_logado)
):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    pasta_templates = os.path.join(base_dir, "..", "templates")
    pasta_temp = os.path.join(base_dir, "..", "temp")

    os.makedirs(pasta_temp, exist_ok=True)

    if ".." in template_nome or "/" in template_nome or "\\" in template_nome:
        raise HTTPException(status_code=400, detail="Nome de template inválido")

    caminho_template = os.path.join(pasta_templates, template_nome)

    if not os.path.exists(caminho_template):
        raise HTTPException(status_code=404, detail="Template não encontrado")

    nome_arquivo = f"proposta_{uuid.uuid4().hex}.pptx"
    caminho_saida = os.path.join(pasta_temp, nome_arquivo)

    try:
        preencher_pptx(caminho_template, caminho_saida, dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    background_tasks.add_task(remover_arquivo, caminho_saida)

    return FileResponse(caminho_saida, filename=f"Proposta_{dados.proposta}.pptx")

# Montar o frontend para ser servido pelo próprio Uvicorn na raiz ("/")
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")