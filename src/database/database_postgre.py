import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carregar as variáveis do .env
load_dotenv()

# Configuração do PostgreSQL
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Criar conexão com o PostgreSQL
def get_engine():
    return create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")