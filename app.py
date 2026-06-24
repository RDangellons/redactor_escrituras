from modulos.generador import generar_compraventa


datos = {
    "escritura": {
        "numero": "Uno(1)",
        "volumen": "I",
        "fecha": "2026-06-24",
        "ciudad": "Tulancingo, Hidalgo",
    },

    "notaria": {
        "notario": "Alejandro Gonzalez Saragoza",
        "notaria_numero": "16",
    },

    "vendedor": {
        "nombre": "ANgel Alonso",
        "nacionalidad": "mexicana",
        "estado_civil": "casado",
        "ocupacion": "comerciante",
        "domicilio": "calle Reforma número 123, colonia Centro, Culiacán, Sinaloa",
        "curp": "PELJ800101HSLRPN09",
        "rfc": "PELJ800101XXX",
        "identificacion": "credencial para votar expedida por el Instituto Nacional Electoral",
    },

    "comprador": {
        "nombre": "MARÍA GARCÍA RUIZ",
        "nacionalidad": "mexicana",
        "estado_civil": "soltera",
        "ocupacion": "empleada",
        "domicilio": "avenida Constitución número 456, colonia Las Quintas, Culiacán, Sinaloa",
        "curp": "GARM900202MSLRZR08",
        "rfc": "GARM900202XXX",
        "identificacion": "credencial para votar expedida por el Instituto Nacional Electoral",
    },

    "inmueble": {
        "ubicacion": "calle Independencia número 789, colonia Centro, Culiacán, Sinaloa",
        "superficie": "doscientos metros cuadrados",
        "medidas_colindancias": "al norte mide diez metros y colinda con lote uno; al sur mide diez metros y colinda con calle Independencia; al oriente mide veinte metros y colinda con lote tres; y al poniente mide veinte metros y colinda con lote cinco",
        "clave_catastral": "001-002-003-004",
        "antecedente_registral": "inscripción número 123, libro 45, sección primera, del Registro Público de la Propiedad",
    },

    "operacion": {
        "precio": "$850,000.00",
        "precio_letra": "ochocientos cincuenta mil pesos 00/100 moneda nacional",
        "forma_pago": "pago de contado",
    }
}


try:
    archivo_generado = generar_compraventa(datos)
    print("Escritura generada correctamente:")
    print(archivo_generado)

except ValueError as error:
    print(error)