SELECT
    o.uf,
    SUM(d.valor_despesa) AS total_despesas,
    ROUND(AVG(d.valor_despesa), 2) AS media_por_operadora
FROM despesas d
JOIN operadoras o ON o.id_operadora = d.id_operadora
GROUP BY o.uf
ORDER BY total_despesas DESC;
