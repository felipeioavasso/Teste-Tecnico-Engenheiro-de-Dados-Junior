const express = require('express');
require('dotenv').config(); // Carrega variáveis do arquivo .env
const mongoose = require('./src/config/mongoose');
const sequelize = require('./src/config/sequelize');
const routes = require('./src/routes/routes'); // Importando as rotas

// Inicializa o Express
const app = express();

// Usa as rotas da API
app.use('/api', routes);

// Inicia o servidor na porta 3000
app.listen(3000, () => {
  console.log('API está rodando na porta 3000');
});
