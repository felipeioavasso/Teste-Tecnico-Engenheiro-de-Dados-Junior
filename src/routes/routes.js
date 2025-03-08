const express = require('express');
const router = express.Router();
const Cliente = require('../models/Cliente');
const Pedido = require('../models/Pedido');

// Rota para listar todos os clientes
router.get('/clientes', async (req, res) => {
  try {
    const clientes = await Cliente.findAll(); // Sequelize
    res.json(clientes);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Rota para buscar pedido no MongoDB por ID
router.get('/pedidos/:id', async (req, res) => {
  try {
    const pedido = await Pedido.findById(req.params.id); // MongoDB
    if (pedido) {
      res.json(pedido);
    } else {
      res.status(404).json({ error: 'Pedido não encontrado' });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
