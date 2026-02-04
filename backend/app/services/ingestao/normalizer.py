import pandas as pd
from app.core.logging import log

COL_MAP = {
    "cnpj": "CNPJ",
    "razao": "RazaoSocial",
    "ano": "Ano",
    "trimestre": "Trimestre",
    "valor": "ValorDespesas",
}


def normalizar(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Mapeia colunas inesperadas para o padrão.
    """
    cols = {}
    for c in chunk.columns:
        key = c.lower()
        for k, v in COL_MAP.items():
            if k in key:
                cols[c] = v

    chunk = chunk.rename(columns=cols)
    chunk = chunk[list(COL_MAP.values())]
    return chunk
