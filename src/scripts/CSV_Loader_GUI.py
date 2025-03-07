import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def carregar_e_exibir_csv():
    dataframe = None  # Variável para armazenar o DataFrame

    def carregar_arquivo():
        nonlocal dataframe
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo CSV", 
            filetypes=[("CSV Files", "*.csv")]
        )
        if arquivo:
            try:
                separador = separador_var.get()
                encoding = encoding_var.get()
                dataframe = pd.read_csv(arquivo, sep=separador, encoding=encoding)
                messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
                exibir_dados(dataframe)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar o arquivo:\n{e}")
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")

    def exibir_dados(df):
        # Exibe os dados no Treeview
        for item in tree.get_children():
            tree.delete(item)
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="w")
        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))

    def enviar_para_notebook():
        nonlocal dataframe
        if dataframe is not None:
            # Exibe uma mensagem de sucesso no Tkinter
            messagebox.showinfo("Sucesso", "Arquivo enviado para o Jupyter Notebook!")

            # Exibe o conteúdo no notebook (no terminal do Jupyter ou em outra célula)
            #print("Arquivo carregado com sucesso no Jupyter!")
            #print(dataframe.head())  # Exibe as primeiras linhas do DataFrame

            # Fecha a janela do Tkinter após enviar os dados
            root.destroy()
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo carregado. Carregue um arquivo primeiro.")

    root = tk.Tk()
    root.title("Carregar Arquivo CSV")
    root.geometry("800x600")

    # Frame para opções de separador e codificação
    frame_opcoes = tk.Frame(root)
    frame_opcoes.pack(pady=10, side="top", fill="x")

    tk.Label(frame_opcoes, text="Separador:").grid(row=0, column=0, padx=5)
    separador_var = tk.StringVar(value=",")
    tk.Entry(frame_opcoes, textvariable=separador_var, width=5).grid(row=0, column=1, padx=5)

    tk.Label(frame_opcoes, text="Codificação:").grid(row=0, column=2, padx=5)
    encoding_var = tk.StringVar(value="utf-8")
    tk.Entry(frame_opcoes, textvariable=encoding_var, width=10).grid(row=0, column=3, padx=5)

    # Frame para os botões
    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10, side="top", fill="x")

    # Botão para carregar arquivo
    botao_carregar = tk.Button(frame_botoes, text="Carregar Arquivo", command=carregar_arquivo)
    botao_carregar.pack(side="left", padx=5)

    # Botão para enviar para notebook
    botao_enviar = tk.Button(frame_botoes, text="Enviar para Notebook", command=enviar_para_notebook)
    botao_enviar.pack(side="left", padx=5)

    # Treeview para exibir dados
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill="both", pady=10)

    # Inicia o loop da interface gráfica
    root.mainloop()

    return dataframe  # Retorna o DataFrame após o loop

# Função para iniciar no Jupyter
if __name__ == "__main__":
    df_jupyter = carregar_e_exibir_csv()  # Captura o DataFrame retornado
    print(df_jupyter.head())  # Exibe as primeiras linhas do DataFrame no Jupyter