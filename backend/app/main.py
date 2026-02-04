from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import configure_logging
from app.db.base import Base
from app.db.session import engine
from app.api import operadoras, despesas, estatisticas
from app.services.ingestao.pipeline import executar_pipeline
import logging

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API Analítica de Operadoras de Saúde",
)

app.include_router(operadoras.router)
app.include_router(despesas.router)
app.include_router(estatisticas.router)


@app.on_event("startup")
def startup():
    logger.info("🚀 Iniciando aplicação")

    logger.info("📦 Criando/verificando tabelas no banco")
    Base.metadata.create_all(bind=engine)

    try:
        logger.info("🔄 Executando pipeline ETL")
        executar_pipeline()
        logger.info("✅ ETL executado com sucesso")
    except Exception as e:
        logger.exception("❌ Erro ao executar ETL")
        raise e

@app.get("/health")
def health_check():
    return {"status": "ok"}
