from fastapi import FastAPI
from app.api.operadoras import router as operadoras_router
from app.api.estatisticas import router as estatisticas_router

app = FastAPI(
    title="ANS Backend",
    version="1.0.0"
)

app.include_router(operadoras_router)
app.include_router(estatisticas_router)
