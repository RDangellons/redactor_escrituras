def obtener_valor(diccionario, ruta):
    partes = ruta.split(".")
    valor = diccionario

    for parte in partes:
        if not isinstance(valor, dict) or parte not in valor:
            return None
        valor = valor[parte]

    return valor


def validar_compraventa(datos):
    campos_obligatorios = {
        "escritura.numero": "Número de escritura",
        "escritura.volumen": "Volumen",
        "escritura.fecha": "Fecha",
        "escritura.ciudad": "Ciudad",

        "notaria.notario": "Nombre del notario",

        "vendedor.nombre": "Nombre del vendedor",
        "vendedor.nacionalidad": "Nacionalidad del vendedor",
        "vendedor.estado_civil": "Estado civil del vendedor",
        "vendedor.domicilio": "Domicilio del vendedor",
        "vendedor.identificacion": "Identificación del vendedor",

        "comprador.nombre": "Nombre del comprador",
        "comprador.nacionalidad": "Nacionalidad del comprador",
        "comprador.estado_civil": "Estado civil del comprador",
        "comprador.domicilio": "Domicilio del comprador",
        "comprador.identificacion": "Identificación del comprador",

        "inmueble.ubicacion": "Ubicación del inmueble",
        "inmueble.superficie": "Superficie del inmueble",
        "inmueble.medidas_colindancias": "Medidas y colindancias",
        "inmueble.antecedente_registral": "Antecedente registral",

        "operacion.precio": "Precio de operación",
        "operacion.precio_letra": "Precio con letra",
        "operacion.forma_pago": "Forma de pago",
    }

    errores = []

    for ruta, nombre in campos_obligatorios.items():
        valor = obtener_valor(datos, ruta)

        if valor is None or str(valor).strip() == "":
            errores.append(f"Falta: {nombre}")

    return errores