import math

# demostracion de uso de funciones math

def mostrar_math(numero):
    #crear una variable
    sen_x = math.sin(numero)
    conse_x = math.cos(numero)
    resultado1 = sen_x * 2 + conse_x * 2

    print("El seno de", numero, "es:", sen_x)
    print("El coseno de", numero, "es:", conse_x)
    print("El resultado de sen^2(x) + cos^2(x) es:", resultado1)

def main():
    numero = float(input("Ingrese un número para calcular su seno y coseno: "))
    mostrar_math(numero)

if __name__ == "__main__":
    main()