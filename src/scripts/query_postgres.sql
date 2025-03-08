SELECT c.nome, SUM(p.total) AS total_gasto
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
GROUP BY c.nome
ORDER BY total_gasto DESC
LIMIT 5;

SELECT
    DATE_TRUNC('month', data_pedido) AS mes,
    ROUND(AVG(total), 2) AS valor_medio_pedidos
FROM pedidos
GROUP BY mes
ORDER BY mes;