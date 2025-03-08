const mongoose = require('mongoose');
require('dotenv').config(); // Carrega as variáveis do arquivo .env

// Configuração do MongoDB com Mongoose
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Conectado ao MongoDB');
}).catch((err) => {
  console.error('Erro ao conectar ao MongoDB:', err);
});
