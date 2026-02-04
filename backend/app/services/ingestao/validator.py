from app.core.logging import log


def validar(registro: dict) -> dict | None:
    valor = registro["ValorDespesas"]

    if valor < 0:
        log.warning("Valor negativo descartado")
        return None

    if valor == 0:
        registro["suspeito"] = True

    if registro["Trimestre"] not in (1, 2, 3, 4):
        log.warning("Trimestre inválido")
        return None

    return registro