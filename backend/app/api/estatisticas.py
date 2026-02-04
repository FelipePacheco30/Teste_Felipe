from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import SessionLocal
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
    total = db.query(func.sum(Despesa.valor_despesas)).scalar() or 0
    media = db.query(func.avg(Despesa.valor_despesas)).scalar() or 0

    top_5 = (
        db.query(
            Despesa.cnpj,
            func.sum(Despesa.valor_despesas).label("total"),
        )
        .group_by(Despesa.cnpj)
        .order_by(func.sum(Despesa.valor_despesas).desc())
        .limit(5)
        .all()
    )

    return {
        "data": {
            "total_despesas": float(total),
            "media_despesas": float(media),
            "top_5_operadoras": [
                {"cnpj": cnpj, "total": float(total)}
                for cnpj, total in top_5
            ],
        }
    }
