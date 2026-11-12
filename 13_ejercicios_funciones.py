ventas_crudas = [
    {
        "id_venta": 1001,
        "cliente": "   mArÍa fErNaNdA lÓpEz  ",
        "email": "maria.lopez@techcorp.pe",
        "subtotal": 250.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4557-8890-1234",
    },
    {
        "id_venta": 1002,
        "cliente": "carlos_ruiz",
        "email": "cruiz_sin_arroba.com",
        "subtotal": 120.0,
        "impuesto": 0.0,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5120-4432-9981",
    },
    {
        "id_venta": 1003,
        "cliente": None,
        "email": "contacto@startup.io",
        "subtotal": -50.0,  # Error de registro (monto negativo)
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4111-2222-3333",
    },
    {
        "id_venta": 1004,
        "cliente": "  ROBERTO GÓMEZ ",
        "email": "rgomez@gmail.com",
        "subtotal": 500.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "CANCELADO",  # Debe filtrarse
        "tarjeta": "4916-0098-7765",
    },
    {
        "id_venta": 1005,
        "cliente": "",
        "email": "ventas@logistica.com",
        "subtotal": 80.0,
        "impuesto": 0.18,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5412-7500-8812",
    },
    {
        "id_venta": 1006,
        "cliente": "  lucía mendieta",
        "email": "lucia@finanzas.pe",
        "subtotal": 5.0,  # Debajo del monto mínimo
        "impuesto": 0.18,
        "moneda": "EUR",  # Moneda no soportada
        "estado": "COMPLETADO",
        "tarjeta": "4000-1234-5678",
    },
]

"""Ejrcicio 1:Eliminar los espacios extra y aplica formato titulo"""
def limpiar_nombre(nombre_crudo: str | None):
    if not nombre_crudo or not nombre_crudo.strip():
        return "Cliente Desconocido"
    return nombre_crudo.strip().title()
    
    
limpiar_nombre(ventas_crudas[0]["cliente"])  # Llamado a la función con el primer cliente de la lista
print(limpiar_nombre(ventas_crudas[0]["cliente"]))  # Imprime el nombre limpio del primer cliente de la lista

"""Ejercicio 2: Extractor de dominio de correo"""
# Input: lucia@finanzas.pe
# Output: finanzas.pe
def extraer_dominio(correo: str):
    if not correo or "@" not in correo:
        return "Correo inválido"
    # split("@") divide el texto en una lista de 2 partes; [-1] toma la última posicion
    return correo.strip().lower().split("@")[-1]  # Extrae el dominio del correo y lo convierte a minúsculas

"""Ejercicio 3: Validador de divisas, solo se permite PEN, USD y montos"""
def es_transaccion_valida(monto: float, moneda: str):
    monedas_permitidas = ["PEN", "USD"]
    if monto >= 0 and moneda.upper() in monedas_permitidas:
        return True
    return False

"""Ejercicio 4: Conversor de divisas con tasa configurable"""

def convertir_a_usd(monto: float, moneda_origen: str, tasa_cambio: float):
    moneda=moneda_origen.upper()
    if moneda=="PEN":
        return round(monto / tasa_cambio, 2)
    if moneda=="USD":
        return round(monto, 2)
    
"""Ejercicio 5: Orquestador del pipeline"""
# 1. Filtrar por el estado del negocio, tiene que estar COMPLETADO
# 2. Limpiar los nombres
# 3. Determinar el dominio
# 4. Validar la transacción
# 5. Convertir a USD si es necesario
# 6. Construir un diccionario de salida

def ejecutar_pipeline(datos_crudos: list[dict]):
    registros_limpios = []
    descartados=0
    monto_total=0
    
    for fila in datos_crudos:
        #1. Filtrar por estado del negocio
        if fila["estado"] != "COMPLETADO":
            descartados+=1
            continue 
        
        #4. Validar la transacción
        if not es_transaccion_valida(fila["subtotal"], fila["moneda"]):
            descartados+=1
            continue
        
        #2. Limpiar los nombres
        fila["cliente"] = limpiar_nombre(fila["cliente"])
        
        #3. Determinar el dominio
        fila["dominio"] = extraer_dominio(fila["email"])
        
        #5. Convertir a USD si es necesario
        fila["subtotal"]= convertir_a_usd(fila["subtotal"], fila["moneda"], 3.5)
        monto_total=monto_total+fila["subtotal"]
        fila["moneda"] = "USD"
        
        registros_limpios.append(fila)
        
    return{
        "data_final": registros_limpios,
        "registros_procesados": len(datos_crudos),
        "registros_descartados": descartados,
        "monto_total_usd": monto_total
    }
    
from pprint import pprint 
resultado=ejecutar_pipeline(ventas_crudas)  # Llamado a la función para ejecutar el pipeline
pprint(resultado)  # Imprime el resultado final del pipeline   
    