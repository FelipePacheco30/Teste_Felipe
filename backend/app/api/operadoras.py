from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.operadora import Operadora
from app.models.despesa import Despesa
from app.schemas.operadora import OperadoraOut

router = APIRouter(prefix="/api/operadoras", tags=["Operadoras"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def listar(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    total = db.query(Operadora).count()
    data = (
        db.query(Operadora)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "data": data,
        "meta": {
            "page": page,
            "limit": limit,
            "total": total
        }
    }

@router.get("/{cnpj}", response_model=OperadoraOut)
def detalhe(cnpj: str, db: Session = Depends(get_db)):
    op = db.get(Operadora, cnpj)
    if not op:
        raise HTTPException(404, "Operadora não encontrada")
    return op

@router.get("/{cnpj}/despesas")
def despesas(cnpj: str, db: Session = Depends(get_db)):
    data = db.query(Despesa).filter(Despesa.cnpj == cnpj).all()
    return {"data": data}
