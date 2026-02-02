from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True)
    cnpj = Column(String(14), index=True)
    ano = Column(Integer)
    trimestre = Column(Integer)
    valor = Column(Numeric(14, 2))
