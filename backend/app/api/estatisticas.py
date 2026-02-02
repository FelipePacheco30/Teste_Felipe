from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.despesa import Despesa

router = APIRouter(prefix="/api/estatisticas", tags=["Estatísticas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def estatisticas(db: Session = Depends(get_db)):
    total = db.query(func.sum(Despesa.valor)).scalar() or 0
    media = db.query(func.avg(Despesa.valor)).scalar() or 0

    top = (
        db.query(
            Despesa.cnpj,
            func.sum(Despesa.valor).label("total")
        )
        .group_by(Despesa.cnpj)
        .order_by(func.sum(Despesa.valor).desc())
        .limit(5)
        .all()
    )

    return {
        "data": {
            "total_despesas": total,
            "media_despesas": media,
            "top_5_operadoras": [
                {"cnpj": c, "total": t} for c, t in top
            ]
        }
    }
