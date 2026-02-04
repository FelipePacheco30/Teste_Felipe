import zipfile
from pathlib import Path
from app.core.logging import log

EXTRACTED_DIR = Path("data/extracted")


def extrair(zip_path: Path):
    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)

    if zipfile.is_zipfile(zip_path):
        log.info(f"Extraindo {zip_path.name}")
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(EXTRACTED_DIR)
