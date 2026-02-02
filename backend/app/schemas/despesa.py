from pydantic import BaseModel
from decimal import Decimal

class DespesaOut(BaseModel):
    ano: int
    trimestre: int
    valor: Decimal
