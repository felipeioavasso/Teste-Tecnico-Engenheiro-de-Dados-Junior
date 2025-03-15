/* Escreva uma consulta MongoDB para retornar os pedidos realizados em fevereiro de 2024. */
db.pedidos.find({
    "data_pedido": { 
      $gte: "2024-02-01", 
      $lt: "2024-03-01"
    }
}).pretty()

/* Escreva uma consulta MongoDB para calcular o total gasto por cliente. */
db.pedidos.aggregate([
{
    $unwind: "$itens"
},
{
    $project: {
    _id: 0,
    Cliente: "$nome",
    "Total Gasto (R$)": { $round: ["$total_gasto", 2] }
    }
},
{
    $sort: { total_gasto: -1 }
}
])
  