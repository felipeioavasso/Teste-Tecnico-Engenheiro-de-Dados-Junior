// src/models/Pedido.js
const mongoose = require('mongoose');

// Definição do modelo de Pedido
const pedidoSchema = new mongoose.Schema({
  clienteId: {
    type: String,
    required: true,
  },
  dataPedido: {
    type: String,
    required: true,
  },
  itens: [
    {
      produto: {
        type: String,
        required: true,
      },
      quantidade: {
        type: Number,
        required: true,
      },
      preco: {
        type: Number,
        required: true,
      }
    }
  ]
});

const Pedido = mongoose.model('Pedido', pedidoSchema);

module.exports = Pedido;
