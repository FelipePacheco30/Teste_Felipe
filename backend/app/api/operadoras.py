from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.operadora import Operadora
from app.models.despesa import Despesa

router = APIRouter(prefix="/api/operadoras", tags=["Operadoras"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def listar_operadoras(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
):
    offset = (page - 1) * limit

    total = db.query(Operadora).count()
    operadoras = (
        db.query(Operadora)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "data": operadoras,
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
        },
    }


@router.get("/{cnpj}")
def obter_operadora(cnpj: str, db: Session = Depends(get_db)):
    operadora = db.get(Operadora, cnpj)
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")

    return {"data": operadora}


@router.get("/{cnpj}/despesas")
def despesas_por_operadora(
    cnpj: str,
    db: Session = Depends(get_db),
):
    despesas = (
        db.query(Despesa)
        .filter(Despesa.cnpj == cnpj)
        .order_by(Despesa.ano, Despesa.trimestre)
        .all()
    )

    if not despesas:
        raise HTTPException(status_code=404, detail="Nenhuma despesa encontrada")

    return {"data": despesas}
