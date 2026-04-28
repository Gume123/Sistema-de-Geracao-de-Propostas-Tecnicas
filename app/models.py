from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    username: str
    password: str
    role: str = "vendedor"


class PropostaData(BaseModel):
    proposta: str = ""
    aleta: str = ""
    diametro_aleta: str = ""
    espacamento: str = ""
    diametro_corpo: str = ""
    aisi: str = ""
    espessura: str = ""
    furo: str = ""
    haste: str = ""
    diametro: str = ""
    preco_unitario: str = ""
    preco_lote: str = ""
    frete_pac: str = ""
    frete_sedex: str = ""
    condiçao_envio: str = ""
    data: str = ""
    nome_vendedor: str = ""
    email_vendedor: str = ""
    nome_cliente: str = ""

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    ativo = Column(Boolean, default=True)
    role = Column(String, default="vendedor")