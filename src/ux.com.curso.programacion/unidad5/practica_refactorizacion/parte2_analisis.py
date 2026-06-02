"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: [Tu Nombre]
"""
import random  # Única librería importada por el novato
import statistics

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    # CAMBIO 1: Se reemplazaron los bucles 'while' que recortaban espacios
    #           por el método .strip() que hace exactamente lo mismo.
    # CAMBIO 2: Se eliminó la conversión manual con ASCII (chr/ord) usando
    #           .capitalize(), que pone mayúscula la primera letra y
    #           minúsculas el resto en una sola operación.
    return nombre_sucio.strip().capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    # CAMBIO: Se reemplazó el doble bucle anidado que comparaba carácter
    #         por carácter por el operador 'in' de Python, que busca
    #         subcadenas de forma optimizada en una sola línea.
    return palabra_prohibida in mensaje_chat


# =====================================================================
# RETO 3: Generador de Contraseñas Temporales
# =====================================================================
def generar_clave_temporal():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    clave_generada = ""
    
    for i in range(8):
        indice_aleatorio = random.randint(0, len(caracteres_validos) - 1)
        caracter_elegido = caracteres_validos[indice_aleatorio]
        clave_generada = clave_generada + caracter_elegido
        
    return clave_generada


# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana)
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    pings_ordenados = list(lista_pings)
    n = len(pings_ordenados)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if pings_ordenados[j] > pings_ordenados[j + 1]:
                temporal = pings_ordenados[j]
                pings_ordenados[j] = pings_ordenados[j + 1]
                pings_ordenados[j + 1] = temporal
                
    if n % 2 == 1:
        return pings_ordenados[n // 2]
    else:
        mitad1 = pings_ordenados[(n // 2) - 1]
        mitad2 = pings_ordenados[n // 2]
        return (mitad1 + mitad2) / 2.0


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte II) ---")
    print("Usuario limpio:", [limpiar_nombre_usuario("   luNA_eDUaRDo  ")])
    msg = "No digas malas palabras en este servidor"
    print("¿Tiene groserías?:", contiene_palabra_bloqueada(msg, "malas"))
    print("Clave generada por el sistema:", generar_clave_temporal())
    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Mediana de latencia encontrada:", calcular_mediana_latencia(pings_servidor))