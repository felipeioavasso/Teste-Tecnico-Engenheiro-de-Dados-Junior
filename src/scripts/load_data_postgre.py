import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from src.database.database_postgre import get_engine

# Caminho do arquivo CSV processado
file_path = "../../data/cleaned_data/Arquivo_CSV_de_Vendas_cleaned.csv"

try:
    # Carregar o dataset modificado
    df = pd.read_csv(file_path)
    print("📂 Dataset carregado com sucesso!")

    # Criar conexão com o banco
    engine = get_engine()

    # Nome da tabela no banco
    table_name = "vendas"

    # Salvar o DataFrame no PostgreSQL
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"✅ Dados inseridos com sucesso na tabela '{table_name}' do PostgreSQL!")

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{file_path}' não foi encontrado. Verifique o caminho.")
except pd.errors.EmptyDataError:
    print("❌ Erro: O arquivo CSV está vazio.")
except pd.errors.ParserError:
    print("❌ Erro: Falha ao processar o arquivo CSV. Verifique o formato.")
except SQLAlchemyError as e:
    print(f"❌ Erro ao inserir dados no PostgreSQL: {e}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
