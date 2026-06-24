from pathlib import Path
from docxtpl import DocxTemplate

from modulos.validaciones import validar_compraventa
from modulos.fechas import fecha_a_letra


BASE_DIR = Path(__file__).resolve().parents[1]


def generar_compraventa(datos):
    errores = validar_compraventa(datos)

    if errores:
        mensaje = "No se puede generar la escritura porque faltan datos:\n"
        mensaje += "\n".join(f"- {error}" for error in errores)
        raise ValueError(mensaje)

    datos["escritura"]["fecha_letra"] = fecha_a_letra(datos["escritura"]["fecha"])

    plantilla = BASE_DIR / "plantillas" / "compraventa.docx"
    carpeta_salida = BASE_DIR / "generadas"

    carpeta_salida.mkdir(exist_ok=True)

    nombre_archivo = f"escritura_{datos['escritura']['numero']}_compraventa.docx"
    ruta_salida = carpeta_salida / nombre_archivo

    doc = DocxTemplate(plantilla)
    doc.render(datos)
    doc.save(ruta_salida)

    return ruta_salida