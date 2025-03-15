import tkinter as tk
import subprocess
import os
import threading
import re

# Caminho do diretório onde o server.js está localizado
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Variável global para armazenar o processo do servidor
server_process = None

def start_server():
    """Inicia o servidor Node.js e captura a porta automaticamente."""
    global server_process
    if server_process is None:
        try:
            server_process = subprocess.Popen(
                ["node", "server.js"],
                cwd=PROJECT_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            status_label.config(text="Iniciando servidor...", fg="blue")

            # Criar uma thread para capturar a saída do servidor
            threading.Thread(target=monitor_output, daemon=True).start()

        except Exception as e:
            status_label.config(text=f"Erro ao iniciar: {e}", fg="red")

def stop_server():
    """Para o servidor Node.js."""
    global server_process
    if server_process:
        server_process.terminate()
        server_process.wait()
        server_process = None
        status_label.config(text="Servidor parado", fg="red")
        port_label.config(text="Porta: --", fg="black")


def monitor_output():
    """Captura a saída do servidor e atualiza a UI."""
    global server_process
    if server_process:
        for line in iter(server_process.stdout.readline, ''):
            line = line.strip()
            if line:
                print(line)  # Exibe no terminal (debug)
                output_text.insert(tk.END, line + "\n")
                output_text.yview(tk.END)

                # Melhorando a regex para capturar a porta corretamente
                match = re.search(r'porta (\d+)', line, re.IGNORECASE)
                if match:
                    porta = match.group(1)
                    port_label.config(text=f"Porta: {porta}", fg="green")
                    status_label.config(text="Servidor rodando", fg="green")


# Criando a interface gráfica
root = tk.Tk()
root.title("Gerenciador do Servidor Node.js")
root.geometry("400x300")

# Criando botões e labels
start_button = tk.Button(root, text="Iniciar Servidor", command=start_server, bg="green", fg="white")
stop_button = tk.Button(root, text="Parar Servidor", command=stop_server, bg="red", fg="white")
status_label = tk.Label(root, text="Servidor parado", fg="red")
port_label = tk.Label(root, text="Porta: --", fg="black")

# Caixa de saída para logs do servidor
output_text = tk.Text(root, height=10, width=50)
output_text.insert(tk.END, "Logs do servidor aparecerão aqui...\n")

# Posicionando elementos na tela
start_button.pack(pady=5)
stop_button.pack(pady=5)
status_label.pack(pady=5)
port_label.pack(pady=5)
output_text.pack(pady=5)

# Executando a interface
root.mainloop()
