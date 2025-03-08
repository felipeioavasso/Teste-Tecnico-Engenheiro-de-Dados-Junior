// src/models/Cliente.js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = require('../config/sequelize'); // Assumindo que a configuração do Sequelize está em src/config/sequelize.js

const Cliente = sequelize.define('clientes', {
  nome: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  }
}, {
  timestamps: false,  // Desabilita as colunas createdAt e updatedAt
});

module.exports = Cliente;
