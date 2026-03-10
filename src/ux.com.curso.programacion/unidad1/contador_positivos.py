#desarrollo de algoritmo contador de positivos

def contador_positivos():
    contador=0
    while True:
        numero = int(input("ingrese un numero(0 para terminar):"))
        if numero <0:
            break
        contador +=1


    print("contador de numeros positivos integrados:", contador)


# definicion de la funcion main (controla el flujo del programa)

def main():
    print("Bienvenido al conrtador de positivos")
    contador_positivos()


    #llamada a la funcion main para inciar el programa
    if __name__ == "__name__":
        main()