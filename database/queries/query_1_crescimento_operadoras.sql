WITH despesas_ordenadas AS (
    SELECT
        d.id_operadora,
        o.razao_social,
        d.ano,
        d.trimestre,
        d.valor_despesa,
        ROW_NUMBER() OVER (
            PARTITION BY d.id_operadora
            ORDER BY d.ano, d.trimestre
        ) AS rn_inicio,
        ROW_NUMBER() OVER (
            PARTITION BY d.id_operadora
            ORDER BY d.ano DESC, d.trimestre DESC
        ) AS rn_fim
    FROM despesas d
    JOIN operadoras o ON o.id_operadora = d.id_operadora
),
inicio_fim AS (
    SELECT
        i.id_operadora,
        i.razao_social,
        i.valor_despesa AS valor_inicial,
        f.valor_despesa AS valor_final
    FROM despesas_ordenadas i
    JOIN despesas_ordenadas f
        ON i.id_operadora = f.id_operadora
    WHERE i.rn_inicio = 1
      AND f.rn_fim = 1
      AND i.valor_despesa > 0
)
SELECT
    razao_social,
    ROUND(((valor_final - valor_inicial) / valor_inicial) * 100, 2) AS crescimento_percentual
FROM inicio_fim
ORDER BY crescimento_percentual DESC
LIMIT 5;
