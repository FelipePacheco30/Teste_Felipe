from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

class DespesaAgregada(Base):
    __tablename__ = "despesas_agregadas"

    id = Column(Integer, primary_key=True)
    cnpj = Column(String(14), index=True)
    ano = Column(Integer)
    trimestre = Column(Integer)
    total_despesas = Column(Numeric(14, 2))
