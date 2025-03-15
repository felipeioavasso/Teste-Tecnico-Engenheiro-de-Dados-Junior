/* • Escreva uma query SQL para recuperar os 5 clientes que mais gastaram em pedidos. */
SELECT c.nome, SUM(p.total) AS total_gasto
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
GROUP BY c.nome
ORDER BY total_gasto DESC
LIMIT 5;

/* • Escreva uma query SQL para obter o valor médio dos pedidos por mês. */
SELECT
    DATE_TRUNC('month', data_pedido) AS mes_ano,
    ROUND(AVG(total), 2) AS valor_medio_pedidos
FROM pedidos
GROUP BY mes_ano
ORDER BY mes;