from sqlalchemy import Column, Integer, String, Numeric
from app.db.base import Base


class DespesaAgregada(Base):
    """
    Dados agregados por operadora / período.
    Gerados pelo ETL.
    """

    __tablename__ = "despesas_agregadas"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), index=True, nullable=False)

    ano = Column(Integer, nullable=False)
    trimestre = Column(Integer, nullable=False)

    total_despesas = Column(Numeric(14, 2), nullable=False)
