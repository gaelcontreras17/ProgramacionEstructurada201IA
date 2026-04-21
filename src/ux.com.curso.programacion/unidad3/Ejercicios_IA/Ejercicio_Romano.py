# Programa para convertir número decimal a romano
# Hecho con funciones básicas

# Función para validar número
def validar_numero(n):
    if n >= 1 and n <= 3000:
        return True
    else:
        return False


# Función para convertir a romano
def convertir_romano(numero):

    resultado = ""

    valores = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]

    romanos = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]

    i = 0

    while i < len(valores):

        while numero >= valores[i]:
            resultado = resultado + romanos[i]
            numero = numero - valores[i]

        i = i + 1

    return resultado


# Programa principal
numero = int(input("Ingresa un número decimal: "))

if validar_numero(numero):
    romano = convertir_romano(numero)
    print("Número romano:", romano)
else:
    print("Error. El número debe estar entre 1 y 3000")

if __name__ == "__main__":
    main()