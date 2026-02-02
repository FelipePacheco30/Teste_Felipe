from datetime import date

def ano_trimestre_from_date(dt: date) -> tuple[int, int]:
    """
    Converte uma data em (ano, trimestre).
    """
    trimestre = (dt.month - 1) // 3 + 1
    return dt.year, trimestre
