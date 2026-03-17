import math



def mostrar_funciones_math():
    numero=20

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)

    print("el seno de", numero, "es:", sen_x)
    print("el coseno de", numero, "es:", conse_x)

    resultado = sen_x ** 2 + conse_x ** 2

    print("El resultado de sen^2(x) + cos^(x) es", resultado)

    def main():
    mostrar_math()

if __name__ == "__main__":
    main()

