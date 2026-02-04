import pandas as pd
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.despesa import Despesa
from app.core.logging import log

PROCESSED = Path("data/processed")
OUTPUT = Path("data/output")


def consolidar(registros: list[dict], db: Session):
    PROCESSED.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(registros)

    csv_path = PROCESSED / "consolidado_despesas.csv"
    df.to_csv(csv_path, index=False)

    zip_path = OUTPUT / "consolidado_despesas.zip"
    df.to_csv(zip_path.with_suffix(".csv"), index=False)

    log.info("Persistindo no banco")

    for r in registros:
        db.add(
            Despesa(
                cnpj=r["CNPJ"],
                razao_social=r["RazaoSocial"],
                ano=r["Ano"],
                trimestre=r["Trimestre"],
                valor_despesas=r["ValorDespesas"],
            )
        )

    db.commit()
