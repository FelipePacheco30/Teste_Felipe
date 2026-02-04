from sqlalchemy import Column, String
from app.db.base import Base


class Operadora(Base):
    """
    Cadastro de operadoras da ANS.
    """

    __tablename__ = "operadoras"

    cnpj = Column(String(14), primary_key=True, index=True)
    razao_social = Column(String, nullable=False)
    uf = Column(String(2), nullable=True)
    status = Column(String, nullable=True)
