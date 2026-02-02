COPY despesas_agregadas (
    uf,
    ano,
    trimestre,
    total_despesas,
    media_por_operadora
)
FROM STDIN
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    NULL '',
    ENCODING 'UTF8'
);
