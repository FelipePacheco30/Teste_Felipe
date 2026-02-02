from pydantic import BaseModel

class OperadoraOut(BaseModel):
    cnpj: str
    razao_social: str
    uf: str | None
    status: str | None

    class Config:
        from_attributes = True
