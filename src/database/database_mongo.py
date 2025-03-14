import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar as variáveis do .env
load_dotenv()

# Configuração do MongoDB a partir do .env
MONGO_URI = os.getenv("MONGO_URI")

def get_mongo_client():
    """Retorna uma conexão com o MongoDB."""
    return MongoClient(MONGO_URI)

def get_mongo_db():
    """Retorna o banco de dados MongoDB."""
    client = get_mongo_client()
    return client.get_database()
