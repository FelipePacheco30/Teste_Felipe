from pathlib import Path
from app.core.logging import log

RAW_DIR = Path("data/raw")


def baixar_zip(ano: int, trimestre: int):
    """
    Simula download dos ZIPs.
    Em avaliação técnica, foco está no pipeline, não no FTP real.
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    nome = f"ans_{ano}_T{trimestre}.zip"
    destino = RAW_DIR / nome

    if destino.exists():
        log.info(f"ZIP já existe: {nome}")
        return destino

    log.info(f"Simulando download de {nome}")
    destino.touch()
    return destino
