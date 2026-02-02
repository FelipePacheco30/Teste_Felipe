from sqlalchemy.orm import Session
from app.models.operadora import Operadora

def enriquecer_com_operadora(
    registro: dict,
    db: Session
) -> dict:
    """
    Enriquecimento por CNPJ.
    """
    operadoras = (
        db.query(Operadora)
        .filter(Operadora.cnpj == registro["cnpj"])
        .all()
    )

    if not operadoras:
        registro["status_enriquecimento"] = "SEM_MATCH"
        return registro

    if len(operadoras) > 1:
        registro["status_enriquecimento"] = "MULTIPLOS_MATCHES"
        return registro

    op = operadoras[0]
    registro["uf"] = op.uf
    registro["status_operadora"] = op.status
    registro["status_enriquecimento"] = "OK"

    return registro
