#ejemplo de repeticion

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana", "banana", "naranja"]
#for para iterar sobre una lista
    for fruta in frutas:
        print(fruta)
#for para iterar sobre un rango de numeros
    for i in range(1,5):
        print(i)
#for para iterar sobre un rango de numeros con un paso
    for i in range(1,10,2):
        print(i)
#estructura WHILE
def ejemplo_while():
    print("Estructura WHILE")
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

#Simulacion de Do While
def ejemplo_do_while():
    print("Estructura Do While")
    secreto = "python12"
    intentos = 0
    while True:
        intentos_usiario = "python12" #simulación de entrada del usuario
        intentos += 1
        if intentos_usiario == secreto:
            print("¡Acceso concedido!")
            break
        else:
            print("¡Acceso denegado! Intenta de nuevo.")
        print ("\n")

def main():
    ejemplo_for()
    print("\n")
    ejemplo_while()
    print("\n")
    ejemplo_do_while()
if __name__ == "__main__":
    main()