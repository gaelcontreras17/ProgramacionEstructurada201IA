#ejemplo apara visualizar la identacion en python 

def explicar_identacio():
    #nivel 1

    mensaje ="Nivel 1 de identacion"
    print(mensaje)

    puntos =10

    if puntos >9:
        #nivel 2
        print ("Entra al flujo de if")

        if puntos ==10:
            #nivel3
            print("puntos es igual a 10")
    
    #cierra nivel 1

def main():
    explicar_identacio()

if __name__ == "__main__":
    main()