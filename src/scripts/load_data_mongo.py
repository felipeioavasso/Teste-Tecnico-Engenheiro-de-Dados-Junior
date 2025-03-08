import pandas as pd
from pymongo.errors import PyMongoError
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.database.database_mongo import get_mongo_db

# Caminho do arquivo CSV processado
file_path = "data/cleaned_data/Arquivo_CSV_de_Vendas_Limpo.csv"

try:
    # Carregar o dataset limpo
    df = pd.read_csv(file_path)
    print("📂 Dataset carregado com sucesso!")

    # Conectar ao MongoDB
    db = get_mongo_db()
    collection_name = "pedidos"
    collection = db[collection_name]

    # Criar dicionário de clientes únicos
    clientes_unicos = {cliente: idx + 1 for idx, cliente in enumerate(df['cliente'].unique())}

    # Criar estrutura de dados para o MongoDB
    vendas = []
    for _, row in df.iterrows():
        venda = {
            "cliente": {
                "id": clientes_unicos[row["cliente"]],
                "nome": row["cliente"]
            },
            "data_pedido": row["data_venda"],
            "itens": [
                {
                    "produto": row["produto"],
                    "quantidade": row["quantidade"],
                    "preco": row["preco_unitario"]
                }
            ]
        }
        vendas.append(venda)

    # Inserir os dados no MongoDB
    collection.insert_many(vendas)
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
