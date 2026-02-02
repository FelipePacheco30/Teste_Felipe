COPY despesas (
    id_operadora,
    ano,
    trimestre,
    valor_despesa
)
FROM STDIN
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    NULL '',
    ENCODING 'UTF8'
);
