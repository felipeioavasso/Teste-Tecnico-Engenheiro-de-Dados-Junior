from pymongo import MongoClient

# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "base_teste_tecnico"

def get_mongo_client():
    """Retorna uma conexão com o MongoDB."""
    return MongoClient(MONGO_URI)

def get_mongo_db():
    """Retorna o banco de dados MongoDB."""
    client = get_mongo_client()
    return client[DB_NAME]
