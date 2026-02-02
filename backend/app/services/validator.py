from app.utils.cnpj import validar_cnpj

def validar_registro(registro: dict) -> list[str]:
    erros = []

    if not validar_cnpj(registro.get("cnpj", "")):
        erros.append("CNPJ inválido")

    if not registro.get("razao_social"):
        erros.append("Razão social vazia")

    valor = registro.get("valor", 0)
    if valor <= 0:
        erros.append("Valor zerado ou negativo")

    if registro.get("trimestre") not in (1, 2, 3, 4):
        erros.append("Trimestre inválido")

    return erros
