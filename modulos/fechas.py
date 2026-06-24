from datetime import datetime
from num2words import num2words


MESES = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}


def fecha_a_letra(fecha_iso):
    """
    Recibe fecha en formato: AAAA-MM-DD
    Ejemplo: 2026-06-24
    Devuelve: veinticuatro de junio de dos mil veintiséis
    """

    fecha = datetime.strptime(fecha_iso, "%Y-%m-%d")

    dia = num2words(fecha.day, lang="es")
    mes = MESES[fecha.month]
    anio = num2words(fecha.year, lang="es")

    return f"{dia} de {mes} de {anio}"