"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: [Tu Nombre]
"""
import random  # Única librería importada por el novato

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    nombre_sin_espacios = ""
    inicio = 0
    fin = len(nombre_sucio) - 1
    
    while inicio <= fin and nombre_sucio[inicio] == " ":
        inicio += 1
    while fin >= inicio and nombre_sucio[fin] == " ":
        fin -= 1
        
    for i in range(inicio, fin + 1):
        nombre_sin_espacios += nombre_sucio[i]
        
    if len(nombre_sin_espacios) > 0:
        primera_letra = nombre_sin_espacios[0]
        if 'a' <= primera_letra <= 'z':
            primera_letra = chr(ord(primera_letra) - 32)
            
        resto_cadena = ""
        for i in range(1, len(nombre_sin_espacios)):
            caracter = nombre_sin_espacios[i]
            if 'A' <= caracter <= 'Z':
                caracter = chr(ord(caracter) + 32)
            resto_cadena += caracter
            
        return primera_letra + resto_cadena
    return ""


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    largo_mensaje = len(mensaje_chat)
    largo_palabra = len(palabra_prohibida)
    
    for i in range(largo_mensaje - largo_palabra + 1):
        coincidencia = True
        for j in range(largo_palabra):
            if mensaje_chat[i + j] != palabra_prohibida[j]:
                coincidencia = False
                break
        if coincidencia:
            return True
            
    return False


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