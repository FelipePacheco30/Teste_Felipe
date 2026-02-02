from sqlalchemy import Column, String
from app.core.database import Base

class Operadora(Base):
    __tablename__ = "operadoras"

    cnpj = Column(String(14), primary_key=True, index=True)
    razao_social = Column(String, nullable=False)
    uf = Column(String(2))
    status = Column(String)
