from datetime import date
from app.core.logging import log


def detectar_ultimos_trimestres(qtd: int = 3) -> list[tuple[int, int]]:
    """
    Retorna os últimos N trimestres (ano, trimestre).
    """
    hoje = date.today()
    ano = hoje.year
    trimestre = (hoje.month - 1) // 3 + 1

    resultado = []

    for _ in range(qtd):
        resultado.append((ano, trimestre))
        trimestre -= 1
        if trimestre == 0:
            trimestre = 4
            ano -= 1

    log.info(f"Trimestres detectados: {resultado}")
    return resultado
