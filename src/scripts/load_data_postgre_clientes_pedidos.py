import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, text
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.database.database_postgre import get_engine

# Caminho do arquivo CSV processado
file_path = "data/cleaned_data/Arquivo_CSV_de_Vendas_Limpo.csv"

try:
    # Carregar o dataset modificado
    df = pd.read_csv(file_path)
    print("\U0001F4C2 Dataset carregado com sucesso!")

    # Criar conexão com o banco
    engine = get_engine()
    
    with engine.begin() as connection:
        try:
            # Inserir dados na tabela de clientes sem duplicatas
            clientes = df[['cliente']].drop_duplicates().reset_index(drop=True)
            
            for _, row in clientes.iterrows():
                stmt = text("""
                    INSERT INTO public.clientes (nome) 
                    SELECT :nome 
                    WHERE NOT EXISTS (
                        SELECT 1 FROM public.clientes WHERE nome = :nome
                    )
                """)
                connection.execute(stmt, {"nome": row['cliente']})
            print("\u2705 Dados de clientes inseridos com sucesso!")
            
            # Mapear clientes para IDs
            result = connection.execute(text("SELECT id, nome FROM public.clientes"))
            clientes_dict = {row.nome: row.id for row in result}
            df['cliente_id'] = df['cliente'].map(clientes_dict)
            
            # Preparar os dados dos pedidos
            pedidos = df[['cliente_id', 'data_venda', 'total_venda']].rename(columns={'data_venda': 'data_pedido', 'total_venda': 'total'})
            
            for _, row in pedidos.iterrows():
                stmt = text("""
                    INSERT INTO public.pedidos (cliente_id, data_pedido, total) 
                    VALUES (:cliente_id, :data_pedido, :total)
                """)
                connection.execute(stmt, {"cliente_id": row['cliente_id'], "data_pedido": row['data_pedido'], "total": row['total']})
            
            print("\u2705 Dados de pedidos inseridos com sucesso!")

        except SQLAlchemyError as e:
            print(f"❌ Erro ao inserir dados no PostgreSQL: {e}")
            raise e

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{file_path}' não foi encontrado. Verifique o caminho.")
except pd.errors.EmptyDataError:
    print("❌ Erro: O arquivo CSV está vazio.")
except pd.errors.ParserError:
    print("❌ Erro: Falha ao processar o arquivo CSV. Verifique o formato.")
except SQLAlchemyError as e:
    print(f"❌ Erro ao conectar ou inserir dados no PostgreSQL: {e}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
