import pandas as pd
from pathlib import Path
from loguru import logger

RAW = Path("data/raw/ans_extracted")
PROCESSED = Path("data/processed")

INCONSISTENCIAS = []

COL_MAP = {
    "CNPJ": "cnpj",
    "RazaoSocial": "razao_social",
    "Ano": "ano",
    "Trimestre": "trimestre",
    "ValorDespesas": "valor"
}

def processar():
    PROCESSED.mkdir(parents=True, exist_ok=True)
    output = PROCESSED / "despesas_enriquecidas.csv"

    frames = []

    for file in RAW.glob("*"):
        logger.info(f"Processando {file.name}")

        if file.suffix == ".csv":
            reader = pd.read_csv(file, chunksize=50000)
        elif file.suffix == ".xlsx":
            reader = [pd.read_excel(file)]
        else:
            continue

        for chunk in reader:
            chunk = chunk.rename(columns=COL_MAP)
            chunk = chunk[list(COL_MAP.values())]

            invalidos = chunk[chunk["valor"] <= 0]
            if not invalidos.empty:
                INCONSISTENCIAS.append(invalidos)

            frames.append(chunk)

    pd.concat(frames).to_csv(output, index=False)
