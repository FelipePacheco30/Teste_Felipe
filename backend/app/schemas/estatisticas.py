from pydantic import BaseModel
from decimal import Decimal

class EstatisticasOut(BaseModel):
    total_despesas: Decimal
    media_despesas: Decimal
    top_5_operadoras: list[dict]
