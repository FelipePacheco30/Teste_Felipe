from fastapi import FastAPI
from app.api.operadoras import router as operadoras_router
from app.api.estatisticas import router as estatisticas_router

app = FastAPI()

app.include_router(operadoras_router, prefix="/api")
app.include_router(estatisticas_router, prefix="/api")
