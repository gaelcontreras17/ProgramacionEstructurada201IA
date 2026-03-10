def imprimir_identificadores():
    nombre_usurario = "Gael" #Inicia con letra y tiene guion bajo
    sensor = "movimiento" # inicia con letra
    _id_interno = 12 # contenedor guion bajo y numeros
    
    print(nombre_usurario)
    print(sensor)
    print(_id_interno)

# nombre correcto de funciones
def calcular_area():
    print("Calculando area...")
    
# definicion de la funcion main
def main():
    imprimir_identificadores()
    calcular_area()
    
# Llamada a la funcion main para iniciar el programa
if __name__ == "__main__":
    main()