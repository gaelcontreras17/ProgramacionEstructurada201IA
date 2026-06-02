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
    # CAMBIO 1: Se reemplazó el bucle manual con concatenación por
    #           random.choices(), que selecciona N elementos al azar
    #           en una sola llamada.
    # CAMBIO 2: Se usa ''.join() para construir la cadena final,
    #           más eficiente que concatenar con + dentro de un bucle.
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    return ''.join(random.choices(caracteres_validos, k=8))


# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana)
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    # CAMBIO 1: Se eliminó el algoritmo de burbuja manual (doble bucle + swap)
    #           y el cálculo manual de la mediana par/impar.
    # CAMBIO 2: Se usa statistics.median() que internamente ordena la lista
    #           y calcula la mediana correctamente en todos los casos.
    return statistics.median(lista_pings)


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte II) ---")
    print("Usuario limpio:", [limpiar_nombre_usuario("   luNA_eDUaRDo  ")])
    msg = "No digas malas palabras en este servidor"
    print("¿Tiene groserías?:", contiene_palabra_bloqueada(msg, "malas"))
    print("Clave generada por el sistema:", generar_clave_temporal())
    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Mediana de latencia encontrada:", calcular_mediana_latencia(pings_servidor))