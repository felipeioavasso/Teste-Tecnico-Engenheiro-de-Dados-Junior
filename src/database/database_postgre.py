from sqlalchemy import create_engine

# Configuração do PostgreSQL
USER = "root"
PASSWORD = "root"
HOST = "localhost"
PORT = "5432"
DB_NAME = "base_teste_tecnico"

# Criar conexão com o PostgreSQL
def get_engine():
    return create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")