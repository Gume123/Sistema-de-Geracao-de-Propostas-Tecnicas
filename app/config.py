from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "chave_secreta_padrao")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

USUARIO = os.getenv("USUARIO", "admin")
SENHA = os.getenv("SENHA", "123456")

# Render passa a variável DATABASE_URL automaticamente com 'postgres://'
# Porém, o SQLAlchemy 1.4+ requer que seja 'postgresql://'
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sistema.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)