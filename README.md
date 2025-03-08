# Teste Técnico – Engenheiro de Dados Júnior

Este repositório contém a solução para o teste técnico de Engenheiro de Dados Júnior, incluindo manipulação de dados, modelagem e querying em banco de dados, além da integração via API REST com Node.js.

## 📌 Objetivo
O projeto tem como objetivo:
1. **Manipulação de Dados com Python**: Processar um arquivo CSV, realizar transformações e salvar os dados no PostgreSQL e MongoDB.
2. **Modelagem e Querying em Bancos de Dados**: Criar queries SQL para PostgreSQL e consultas no MongoDB.
3. **Integração de Dados com Node.js**: Criar uma API REST para interação com PostgreSQL e MongoDB.

---

## 🚀 Tecnologias Utilizadas
- **Python** (para manipulação de dados)
- **Pandas** (processamento de CSV)
- **Docker** (containerização do ambiente e banco de dados)
- **PostgreSQL** + **SQLAlchemy** (armazenamento relacional)
- **MongoDB** + **PyMongo** (armazenamento NoSQL)
- **Node.js** + **Express.js** (API REST)
- **Sequelize** (ORM para PostgreSQL)
- **Mongoose** (ODM para MongoDB)

---

## 📄 Estrutura do Projeto
```
/
├── data/                    # Arquivos de dados CSV
│   ├── raw_data/            # Dados brutos
│   ├── cleaned_data/        # Dados processados
├── src/                     # Código-fonte do projeto
│   ├── config/              # Configurações do banco de dados
│   ├── database/            # Conexão com PostgreSQL e MongoDB
│   ├── models/              # Modelos do banco de dados
│   │   ├── Cliente.js
│   │   ├── Pedido.js
│   ├── routes/              # Rotas da API
│   │   ├── routes.js
│   ├── scripts/             # Scripts de manipulação de dados
│   │   ├── analisando_dados.ipynb
│   │   ├── load_data_mongo.py
│   │   ├── load_data_postgre_clientes_pedidos.py
│   │   ├── query_mongo.js
│   │   ├── query_postgres.sql
├── .gitignore               # Arquivos ignorados pelo Git
├── .env                     # Configuração de ambiente (não incluído no repositório)
├── README.md                # Documentação do projeto
├── package.json             # Dependências do Node.js
├── package-lock.json        # Controle de versões dos pacotes
└── server.js                # Arquivo principal da API
```
---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/felipeioavasso/Teste-Tecnico-Engenheiro-de-Dados-Junior.git
cd Teste-Tecnico-Engenheiro-de-Dados-Junior
```
---

![image](https://github.com/user-attachments/assets/ba52b465-bab0-43f1-b172-4e8e7d6f87e9)



### 📊 Coleta e Visualização dos Dados  

🔹 Coleta de Dados

Para carregar os dados, foi criada uma interface gráfica com Tkinter, permitindo a importação de arquivos CSV de forma interativa. O script responsável por essa funcionalidade é o CSV_loader_GUI.py.

🔹 Visualização dos Dados com Streamlit

Para analisar rapidamente os dados, foi desenvolvido um aplicativo em Streamlit.
Como Rodar o Streamlit:
 1. Navegue até o diretório do arquivo:
```
    cd src/scripts
```

 2. Execute o seguinte comando:
```
    streamlit run streamlit_analyzer_data.py
```
 3. Acesse a aplicação em seu navegador:
    Se não abrir automaticamente, vá até http://localhost:8501.

### 🔄 Transformação e Armazenamento de Dados
🔹 Transformações Realizadas  

Todas as transformações aplicadas aos dados estão documentadas no Jupyter Notebook `analisando_dados.ipynb`. Algumas das etapas incluem:  
✅ Normalização de dados  
✅ Criação de novas colunas derivadas  

🔹 Salvando os Dados no PostgreSQL e MongoDB
### 📥 Carregamento dos Dados nos Bancos de Dados

Após a transformação, os dados são carregados nos bancos de dados:

✅ PostgreSQL:
Execute o seguinte comando para carregar os dados no PostgreSQL:
```
python src/scripts/load_data_postgre_clientes_pedidos.py
```
✅ MongoDB:
Execute o seguinte comando para carregar os dados no MongoDB:
```
python src/scripts/load_data_mongo.py
```

Os dados foram carregados conforme requisitado:

    PostgreSQL (Tópico 2, Parte 1):
![image](https://github.com/user-attachments/assets/118a9347-a6f9-4d98-8006-7b461f154e2a)

    MongoDB (Tópico 2, Parte 2):
![image](https://github.com/user-attachments/assets/72815cfe-b7db-4046-8a62-79ca9e925fdc)


### 🔎 Consultas no Banco de Dados  

As queries para consulta estão disponíveis no diretório scripts:  
![image](https://github.com/user-attachments/assets/05df8f42-8b61-43dd-93a7-3e6e20d528cb)

  
### 🔗 Integração de Dados com Node.js

Para a implementação da integração de dados via API REST com Node.js, os seguintes arquivos são essenciais:
![image](https://github.com/user-attachments/assets/a671dfd4-cff3-43dd-be15-cedbb4a510ff)

- **`server.js`** – Arquivo principal da aplicação, responsável por iniciar o servidor Node.js e configurar as rotas da API.  
- **`routes/routes.js`** – Define as rotas da API para comunicação com os bancos de dados.  
- **`config/mongoose.js e sequelize.js`** – Configuração das conexões com MongoDB e PostgreSQL.  
- **`models/Cliente.js`** – Modelo de dados do cliente, utilizado para operações no banco.  
- **`models/Pedido.js`** – Modelo de dados do pedido, representando as transações no sistema.  
- **`package.json`** – Contém as dependências do projeto e scripts para execução do servidor.  
- **`package-lock.json`** – Controle de versões dos pacotes instalados no projeto.  




## 📌 Contato
Caso tenha dúvidas ou sugestões, entre em contato!

---

**Felipe Ioavasso**  
📧 Email: [felipeioavasso@gmail.com](mailto:felipeioavasso@gmail.com)  
🔗 GitHub: [github.com/felipeioavasso](https:https://github.com/felipeioavasso/Teste-Tecnico-Engenheiro-de-Dados-Junior)
