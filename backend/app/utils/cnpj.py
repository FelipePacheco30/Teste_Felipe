import re

def validar_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r"\D", "", cnpj)
    if len(cnpj) != 14:
        return False

    def calc_digitos(cnpj, pesos):
        s = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        r = 11 - (s % 11)
        return "0" if r >= 10 else str(r)

    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos2 = [6] + pesos1

    d1 = calc_digitos(cnpj, pesos1)
    d2 = calc_digitos(cnpj + d1, pesos2)

    return cnpj[-2:] == d1 + d2
