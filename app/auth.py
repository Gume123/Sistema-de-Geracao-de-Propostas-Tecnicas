from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from .crypt import pwd_context, verificar_senha

from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, USUARIO, SENHA
from sqlalchemy.orm import Session
from .database import get_db
from .models import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def criar_token(dados: dict, expira_em: timedelta | None = None):

    dados_para_token = dados.copy()

    if expira_em:
        expire = datetime.utcnow() + expira_em
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    dados_para_token.update({"exp": expire})

    return jwt.encode(dados_para_token, SECRET_KEY, algorithm=ALGORITHM)

async def login_usuario(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()

    if not user or not verificar_senha(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
        
    if not user.ativo:
        raise HTTPException(status_code=401, detail="Usuário inativo")

    access_token = criar_token(
        {"sub": form_data.username},
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "token_type": "bearer"}


async def usuario_logado(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = payload.get("sub")

        if usuario is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return usuario

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    
