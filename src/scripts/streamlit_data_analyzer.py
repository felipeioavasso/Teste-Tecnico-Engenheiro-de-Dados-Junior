import os
import pandas as pd
import streamlit as st
from tkinter import Tk, filedialog, messagebox
import os  # Para usar os._exit()

# Definindo algumas cores suaves para as mensagens
SUCCESS_COLOR = "background-color: #e9f7ef; color: #2d6a4f;"  # Verde claro para sucesso
WARNING_COLOR = "background-color: #fff3cd; color: #856404;"  # Amarelo suave para alertas
ERROR_COLOR = "background-color: #f8d7da; color: #721c24;"    # Vermelho suave para erros

# Função para selecionar múltiplos diretórios com Tkinter
def select_directories():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    messagebox.showinfo("Bem-vindo", "Bem-vindo ao seletor de diretórios!")

    directories = []
    while True:
        directory = filedialog.askdirectory(title="Selecione um diretório")
        if directory:
            directories.append(directory)
            msg = f"Diretório selecionado: {directory}\n\nDeseja selecionar mais algum diretório?"
            if not messagebox.askyesno("Selecionar mais", msg):
                break
        else:
            break

    root.destroy()  # Fecha o contexto do Tkinter
    return directories

# Função para listar todos os arquivos CSV em um diretório e seus subdiretórios
def get_all_csv_files(directory):
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files

# Função para carregar os diretórios usando cache do Streamlit
@st.cache_data
def load_directories():
    return select_directories()

# Função para verificar dados ausentes
def verifica_dados_ausentes(file_name, df):
    df_cleaned = df.drop(columns=[col for col in df.columns if 'Unnamed' in col], errors='ignore')

    missing_data = df_cleaned.isnull().sum()
    missing_info = missing_data[missing_data > 0]

    if missing_info.empty:
        st.markdown(f"<div style='{SUCCESS_COLOR}'>Arquivo: {file_name}<br>Não foram encontrados dados ausentes.</div>", unsafe_allow_html=True)
    else:
        missing_info_formatted = missing_info.to_frame(name="Dados Ausentes")
        missing_info_formatted.index.name = 'Coluna'

        st.markdown(f"<div style='{WARNING_COLOR}'>Arquivo: {file_name}<br>Dados Ausentes:</div>", unsafe_allow_html=True)
        st.dataframe(missing_info_formatted)

        total_missing = missing_info.sum()
        st.markdown(f"<div style='{WARNING_COLOR}'>Total de dados ausentes: {total_missing:,}</div>", unsafe_allow_html=True)

# Função para verificar dados duplicados
def verifica_dados_duplicados(file_name, df):
    df_cleaned = df.drop(columns=[col for col in df.columns if 'Unnamed' in col], errors='ignore')

    duplicated_data = df_cleaned[df_cleaned.duplicated()]

    if duplicated_data.empty:
        st.markdown(f"<div style='{SUCCESS_COLOR}'>Arquivo: {file_name}<br>Não foram encontrados dados duplicados.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='{WARNING_COLOR}'>Arquivo: {file_name}<br>Dados Duplicados:</div>", unsafe_allow_html=True)
        st.dataframe(duplicated_data)

        total_duplicated = duplicated_data.shape[0]
        st.markdown(f"<div style='{WARNING_COLOR}'>Total de dados duplicados: {total_duplicated:,}</div>", unsafe_allow_html=True)

# Função para encerrar o servidor Streamlit de forma controlada
def stop_streamlit():
    st.warning("Servidor encerrado...")
    os._exit(0)  # Encerra o processo Python do Streamlit imediatamente

# Início do programa
st.title("Explorador de Dados Personalizado")

selected_dirs = load_directories()

if not selected_dirs:
    st.warning("Nenhum diretório foi selecionado. Por favor, reinicie o aplicativo e escolha pelo menos um diretório.")
else:
    directories = {os.path.basename(dir_path): dir_path for dir_path in selected_dirs}

    category_option = st.sidebar.selectbox(
        "Escolha a pasta:",
        list(directories.keys())
    )

    if category_option:
        selected_dir = directories[category_option]

        csv_files = get_all_csv_files(selected_dir)

        if csv_files:
            file_option = st.sidebar.selectbox(
                "Escolha um arquivo:",
                [os.path.relpath(f, selected_dir) for f in csv_files]
            )

            if file_option:
                file_path = os.path.join(selected_dir, file_option)

                try:
                    # Tenta detectar a codificação correta do arquivo
                    encodings = ["utf-8", "latin1", "ISO-8859-1", "cp1252"]
                    for encoding in encodings:
                        try:
                            df = pd.read_csv(file_path, encoding=encoding, sep=None, engine="python")
                            break
                        except Exception:
                            continue

                    view_option = st.sidebar.radio(
                        "Escolha a visualização:",
                        ("Visualizar Dados", "Informações Gerais", "Estatísticas Descritivas", "Verificar Dados Ausentes", "Verificar Dados Duplicados")
                    )

                    if view_option == "Visualizar Dados":
                        st.dataframe(df)
                    elif view_option == "Informações Gerais":
                        st.markdown(f'<h3>Informações Gerais sobre: {file_option}</h3>', unsafe_allow_html=True)

                        st.write("### Estrutura do DataFrame:")
                        st.write(f"- **Número de Linhas**: {df.shape[0]:,}".replace(",", "."))
                        st.write(f"- **Número de Colunas**: {df.shape[1]:,}".replace(",", "."))
                        st.write(f"- **Uso de Memória**: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

                        info_df = pd.DataFrame({
                            "Coluna": df.columns,
                            "Não Nulos": [f"{val:,}".replace(",", ".") for val in df.notnull().sum()],
                            "Tipo de Dado": df.dtypes.astype(str)
                        })
                        st.dataframe(info_df)

                        st.write("### Primeiras Linhas do DataFrame:")
                        st.dataframe(df.head())

                    elif view_option == "Estatísticas Descritivas":
                        st.markdown(f'<h3>Estatísticas Descritivas de: {file_option}</h3>', unsafe_allow_html=True)
                        st.write(df.describe())

                    elif view_option == "Verificar Dados Ausentes":
                        st.markdown(f'<h3>Verificando Dados Ausentes em: {file_option}</h3>', unsafe_allow_html=True)
                        verifica_dados_ausentes(file_option, df)

                    elif view_option == "Verificar Dados Duplicados":
                        st.markdown(f'<h3>Verificando Dados Duplicados em: {file_option}</h3>', unsafe_allow_html=True)
                        verifica_dados_duplicados(file_option, df)

                except Exception as e:
                    st.markdown(f"<div style='{ERROR_COLOR}'>Erro ao carregar o arquivo: {e}</div>", unsafe_allow_html=True)
        else:
            st.warning("Nenhum arquivo CSV encontrado no diretório selecionado e seus subdiretórios.")

# Botão para encerrar o servidor Streamlit na barra lateral
if st.sidebar.button("Encerrar o Streamlit"):
    stop_streamlit()  # Chama a função que encerra o Streamlit de forma controlada