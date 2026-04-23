# Archivo: analizador_ia.py

# Función para normalizar mensaje
def normalizar_mensaje(texto):
    return texto.lower().strip()


# Función para detectar intención
def detectar_intencion(mensaje):

    if "encender" in mensaje or "activar" in mensaje or "reproducir" in mensaje:
        return "COMANDO DE ACCIÓN"

    elif "ayuda" in mensaje or "error" in mensaje or "fallo" in mensaje:
        return "REPORTE DE SOPORTE"

    else:
        return "CONSULTA GENERAL"


# Programa principal
mensaje_original = input()

longitud = len(mensaje_original)

mensaje_limpio = normalizar_mensaje(mensaje_original)

categoria = detectar_intencion(mensaje_limpio)

print(mensaje_limpio)
print(categoria)
print(longitud)