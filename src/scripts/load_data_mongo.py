import pandas as pd
from pymongo.errors import PyMongoError
from src.database.database_mongo import get_mongo_db

# Caminho do arquivo CSV processado
file_path = "../../data/cleaned_data/Arquivo_CSV_de_Vendas_cleaned.csv"

try:
    # Carregar o dataset modificado
    df = pd.read_csv(file_path)
    print("📂 Dataset carregado com sucesso!")

    # Conectar ao MongoDB
    db = get_mongo_db()
    collection_name = "vendas"
    collection = db[collection_name]

    # Converter DataFrame para dicionários e inserir no MongoDB
    data = df.to_dict(orient="records")
    collection.insert_many(data)

    print(f"✅ Dados inseridos com sucesso na coleção '{collection_name}' do MongoDB!")

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{file_path}' não foi encontrado. Verifique o caminho.")
except pd.errors.EmptyDataError:
    print("❌ Erro: O arquivo CSV está vazio.")
except pd.errors.ParserError:
    print("❌ Erro: Falha ao processar o arquivo CSV. Verifique o formato.")
except PyMongoError as e:
    print(f"❌ Erro ao inserir dados no MongoDB: {e}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
