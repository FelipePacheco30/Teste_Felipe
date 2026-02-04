from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.despesa import Despesa

router = APIRouter(prefix="/api/despesas", tags=["Despesas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def listar_despesas(
    ano: int | None = Query(None),
    trimestre: int | None = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Despesa)

    if ano:
        query = query.filter(Despesa.ano == ano)
    if trimestre:
        query = query.filter(Despesa.trimestre == trimestre)

    total = query.count()
    offset = (page - 1) * limit

    despesas = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "data": despesas,
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
        },
    }
