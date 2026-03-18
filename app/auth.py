from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, USUARIO, SENHA

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def criar_token(dados: dict, expira_em: timedelta | None = None):

    dados_para_token = dados.copy()

    if expira_em:
        expire = datetime.utcnow() + expira_em
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    dados_para_token.update({"exp": expire})

    return jwt.encode(dados_para_token, SECRET_KEY, algorithm=ALGORITHM)


async def login_usuario(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username != USUARIO or form_data.password != SENHA:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

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
    
