
CREATE TABLE operadoras (
    id_operadora      SERIAL PRIMARY KEY,
    cnpj              CHAR(14) NOT NULL UNIQUE,
    razao_social      TEXT NOT NULL,
    nome_fantasia     TEXT,
    uf                CHAR(2) NOT NULL,
    data_cadastro     DATE,
    situacao          TEXT
);

COMMENT ON TABLE operadoras IS 'Cadastro das operadoras de saúde';
COMMENT ON COLUMN operadoras.cnpj IS 'CNPJ sem máscara';

CREATE TABLE despesas (
    id_despesa        SERIAL PRIMARY KEY,
    id_operadora      INTEGER NOT NULL REFERENCES operadoras(id_operadora),
    ano               INTEGER NOT NULL,
    trimestre         INTEGER NOT NULL CHECK (trimestre BETWEEN 1 AND 4),
    valor_despesa     DECIMAL(15,2) NOT NULL,

    CONSTRAINT uk_operadora_periodo UNIQUE (id_operadora, ano, trimestre)
);

COMMENT ON TABLE despesas IS 'Despesas consolidadas por operadora, ano e trimestre';


CREATE TABLE despesas_agregadas (
    id_agregada       SERIAL PRIMARY KEY,
    uf                CHAR(2) NOT NULL,
    ano               INTEGER NOT NULL,
    trimestre         INTEGER NOT NULL CHECK (trimestre BETWEEN 1 AND 4),
    total_despesas    DECIMAL(15,2) NOT NULL,
    media_por_operadora DECIMAL(15,2) NOT NULL
);

COMMENT ON TABLE despesas_agregadas IS 'Despesas agregadas por UF e período';
