from pathlib import Path
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, messagebox
from docxtpl import DocxTemplate


BASE_DIR = Path(__file__).resolve().parent

RUTA_PLANTILLA = BASE_DIR / "plantilla.docx"
CARPETA_GENERADAS = BASE_DIR / "generadas"


def generar_escritura():
    vendedor_nombre = entrada_vendedor.get().strip()
    comprador_nombre = entrada_comprador.get().strip()

    if not vendedor_nombre:
        messagebox.showerror("Dato faltante", "Captura el nombre del vendedor.")
        return

    if not comprador_nombre:
        messagebox.showerror("Dato faltante", "Captura el nombre del comprador.")
        return

    if not RUTA_PLANTILLA.exists():
        messagebox.showerror(
            "Plantilla no encontrada",
            "No se encontró el archivo plantilla.docx."
        )
        return

    datos = {
        "datosPV": {
            "nombre": vendedor_nombre.upper()
        },
        "datosPC": {
            "nombre": comprador_nombre.upper()
        }
    }

    try:
        CARPETA_GENERADAS.mkdir(exist_ok=True)

        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"escritura_generada_{fecha_archivo}.docx"
        ruta_salida = CARPETA_GENERADAS / nombre_archivo

        doc = DocxTemplate(RUTA_PLANTILLA)
        doc.render(datos)
        doc.save(ruta_salida)

        messagebox.showinfo(
            "Escritura generada",
            f"La escritura se generó correctamente:\n\n{ruta_salida}"
        )

        entrada_vendedor.delete(0, "end")
        entrada_comprador.delete(0, "end")

    except Exception as error:
        messagebox.showerror(
            "Error al generar",
            f"Ocurrió un error:\n\n{error}"
        )


# Ventana principal
ventana = Tk()
ventana.title("Redactor de Escrituras")
ventana.geometry("500x260")
ventana.resizable(False, False)

Label(
    ventana,
    text="Sistema Redactor de Escrituras",
    font=("Arial", 16, "bold")
).pack(pady=15)

Label(
    ventana,
    text="Nombre completo del vendedor:",
    font=("Arial", 11)
).pack()

entrada_vendedor = Entry(ventana, width=55, font=("Arial", 11))
entrada_vendedor.pack(pady=5)

Label(
    ventana,
    text="Nombre completo del comprador:",
    font=("Arial", 11)
).pack()

entrada_comprador = Entry(ventana, width=55, font=("Arial", 11))
entrada_comprador.pack(pady=5)

Button(
    ventana,
    text="Generar escritura",
    font=("Arial", 12, "bold"),
    width=25,
    command=generar_escritura
).pack(pady=20)

ventana.mainloop()