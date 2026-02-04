from sqlalchemy.orm import Session
from app.core.logging import log
from app.models.despesa import Despesa
from app.services.ingestao.detector import detectar_ultimos_trimestres
from app.services.ingestao.downloader import baixar_zip
from app.services.ingestao.extractor import extrair


def etl_ja_executado(db: Session) -> bool:
    return db.query(Despesa).first() is not None


def executar_etl(db: Session):
    if etl_ja_executado(db):
        log.info("ETL já executado. Pulando.")
        return

    log.info("Iniciando ETL")

    trimestres = detectar_ultimos_trimestres()

    for ano, tri in trimestres:
        zip_path = baixar_zip(ano, tri)
        extrair(zip_path)

    log.info("ETL finalizado com sucesso")
