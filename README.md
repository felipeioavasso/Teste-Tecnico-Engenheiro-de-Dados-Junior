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

imagem(colocar)


A primeira etapa do trabalho foi a coleta dos dados. Para isso, utilizamos uma interface gráfica desenvolvida em Python com Tkinter, que permite carregar arquivos CSV de forma interativa. A função `carregar_e_exibir_csv` foi criada para carregar o arquivo.
Para ler o arquivo foi utilizado o arquivo CSV_Loader_GUI.

O streamlit_data_analyzer é uma maneirar rápida e fácil de visualizar o dataset e suas principais informações.

## Como Ativar a Visualização dos Datasets no Streamlit
1. **Acesse o Diretório do Arquivo**
   
   Abra o terminal e navegue até a pasta onde o arquivo `streamlit_analysier_data.py` está localizado. Para isso, use o comando `cd` (mudar diretório) para acessar o caminho correto da pasta. Exemplo:

   ```bash 
   cd /caminho/para/a/pasta/do/arquivo/streamlit_analysier_data.py

2. Execute o Comando do Streamlit

   Uma vez no diretório correto, execute o seguinte comando para rodar o aplicativo Streamlit:
   streamlit run streamlit_analysier_data.py

3. Acessando a Aplicação

   Após rodar o comando, o Streamlit abrirá automaticamente a aplicação em seu navegador padrão. Caso não abra automaticamente, você poderá acessar manualmente o endereço abaixo em qualquer navegador:
   http://localhost:8501














## 📌 Contato
Caso tenha dúvidas ou sugestões, entre em contato!

---

**Felipe Ioavasso**  
📧 Email: [felipeioavasso@gmail.com](mailto:felipeioavasso@gmail.com)  
🔗 GitHub: [github.com/felipeioavasso](https:https://github.com/felipeioavasso/Teste-Tecnico-Engenheiro-de-Dados-Junior)
