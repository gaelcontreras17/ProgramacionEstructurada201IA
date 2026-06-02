"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: [Tu Nombre]
"""
import math  # El novato solo importó math esta vez

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# Sentido: Crear una cuadrícula vacía de 4x4 (como el juego 2048 o un tablero)
#          inicializada con ceros antes de colocar las piezas de la IA.
# Problema: Uso erróneo y peligroso de multiplicación de referencias,
#           o bucles anidados manuales sumamente redundantes.
# =====================================================================
def inicializar_tablero_vacio():
    # CAMBIO 1: Se eliminó la creación con multiplicación de referencias
    #           (era un bug clásico en Python: todas las filas apuntaban a la
    #           misma dirección de memoria, así que modificar una afectaba a todas).
    # CAMBIO 2: Se usa list comprehension para crear 4 filas independientes
    #           en una sola línea, eliminando también el bucle redundante de "limpieza".
    return [[0] * 4 for _ in range(4)]

# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# Sentido: Limitar las señales de los sensores del robot a un rango seguro.
#          Si la señal baja de un mínimo o pasa de un máximo, se "recorta".
# Problema: Lógica condicional repetitiva y tosca que ignora funciones nativas.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    # CAMBIO: Se reemplazó el if/else anidado por la combinación
    #         max(minimo, min(valor_lectura, maximo)), que es el modismo
    #         clásico de "clamp" (recortar a un rango) en una sola línea.
    return max(minimo, min(valor_lectura, maximo))

# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# Sentido: Encontrar el menor error absoluto (loss) en una lista de pruebas.
# Problema: Inicialización incorrecta o manual de infinitos y cálculo 
#           tosco del valor absoluto usando multiplicaciones por -1.
# =====================================================================
def buscar_error_minimo(lista_errores):
    # El novato inicializa el menor error con un número "grande" inventado
    menor_error = 999999.99 
    
    for i in range(len(lista_errores)):
        valor_actual = lista_errores[i]
        
        # Intento manual de obtener el valor absoluto (fabs)
        if valor_actual < 0:
            absoluto = valor_actual * -1
        else:
            absoluto = valor_actual
            
        if absoluto < menor_error:
            menor_error = absoluto
            
    return menor_error

# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# Sentido: Limpiar las IDs de los usuarios del servidor de Discord para
#          que no se procesen comandos repetidos en el mismo ciclo.
# Problema: Algoritmo de búsqueda lineal doblemente anidado sumamente lento.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    lista_limpia = []
    
    # Recorrido manual buscando si el elemento ya existe antes de agregarlo
    for i in range(len(lista_ids)):
        id_actual = lista_ids[i]
        ya_existe = False
        
        for j in range(len(lista_limpia)):
            if lista_limpia[j] == id_actual:
                ya_existe = True
                break
                
        if not ya_existe:
            lista_limpia.append(id_actual)
            
    return lista_limpia


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte III) ---")
    
    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)
        
    print("Lectura recortada (125.4 en rango 0-100):", limitar_senal_sensor(125.4, 0.0, 100.0))
    
    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print("El error más cercano a cero es:", buscar_error_minimo(errores_entrenamiento))
    
    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print("Lista de IDs únicas filtradas:", depurar_usuarios_repetidos(ids_discord))