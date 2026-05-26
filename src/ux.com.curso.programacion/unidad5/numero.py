n = int(input())

def es_raro(numero):
    if numero % 2 != 0:
        return "Weird"
    else:
        if numero >= 2 and numero <= 5:
            return "Not Weird"
        elif numero >= 6 and numero <= 20:
            return "Weird"
        else:
            return "Not Weird"

resultado = es_raro(n)
print(resultado)