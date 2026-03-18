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

    caminho_template = os.path.join("templates", template_nome)

    if not os.path.exists(caminho_template):
        raise HTTPException(status_code=404, detail="Template não encontrado")

    nome_arquivo = f"proposta_{uuid.uuid4().hex}.pptx"

    caminho_saida = os.path.join("temp", nome_arquivo)

    preencher_pptx(caminho_template, caminho_saida, dados.dict())

    background_tasks.add_task(remover_arquivo, caminho_saida)

    return FileResponse(caminho_saida, filename=f"Proposta_{dados.proposta}.pptx")