/* Escreva uma consulta MongoDB para retornar os pedidos realizados em fevereiro de 2024. */
db.pedidos.find({
    "data_pedido": { 
      $gte: "2024-02-01", 
      $lt: "2024-03-01"
    }
})

/* Escreva uma consulta MongoDB para calcular o total gasto por cliente. */
db.pedidos.aggregate([
{
    $unwind: "$itens"
},
{
    $group: {
    _id: "$cliente.id",
    nome: { $first: "$cliente.nome" },
    total_gasto: { $sum: { $multiply: ["$itens.quantidade", "$itens.preco"] } }
    }
},
{
    $sort: { total_gasto: -1 }
}
])
  