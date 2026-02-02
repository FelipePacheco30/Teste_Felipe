WITH media_trimestre AS (
    SELECT
        ano,
        trimestre,
        AVG(valor_despesa) AS media_geral
    FROM despesas
    GROUP BY ano, trimestre
),
comparacao AS (
    SELECT
        d.id_operadora,
        d.ano,
        d.trimestre,
        d.valor_despesa,
        m.media_geral,
        CASE
            WHEN d.valor_despesa > m.media_geral THEN 1
            ELSE 0
        END AS acima_media
    FROM despesas d
    JOIN media_trimestre m
      ON d.ano = m.ano
     AND d.trimestre = m.trimestre
),
contagem AS (
    SELECT
        id_operadora,
        COUNT(*) FILTER (WHERE acima_media = 1) AS trimestres_acima
    FROM comparacao
    GROUP BY id_operadora
)
SELECT
    COUNT(*) AS total_operadoras
FROM contagem
WHERE trimestres_acima >= 2;
