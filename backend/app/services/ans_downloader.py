from pathlib import Path
import zipfile
from loguru import logger

RAW_ZIP = Path("data/raw/ans_zip")
RAW_EXTRACTED = Path("data/raw/ans_extracted")

def extrair_arquivos():
    RAW_EXTRACTED.mkdir(parents=True, exist_ok=True)

    for zip_file in RAW_ZIP.glob("*.zip"):
        logger.info(f"Extraindo {zip_file.name}")
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(RAW_EXTRACTED)
