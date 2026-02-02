CREATE INDEX idx_operadoras_cnpj ON operadoras(cnpj);
CREATE INDEX idx_operadoras_uf ON operadoras(uf);

CREATE INDEX idx_despesas_periodo ON despesas(ano, trimestre);
CREATE INDEX idx_despesas_operadora ON despesas(id_operadora);

CREATE INDEX idx_agregadas_uf_periodo ON despesas_agregadas(uf, ano, trimestre);
