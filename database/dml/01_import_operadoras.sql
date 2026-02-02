COPY operadoras (
    cnpj,
    razao_social,
    nome_fantasia,
    uf,
    data_cadastro,
    situacao
)
FROM STDIN
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    NULL '',
    ENCODING 'UTF8'
);
