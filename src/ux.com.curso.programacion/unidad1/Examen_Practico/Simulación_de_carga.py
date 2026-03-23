def main():
    suma = 0
    contador = 0

    print("Filtrado de Outliers (10 lecturas)")

    for i in range(10):
        try:
            lectura = float(input(f"Ingresa la lectura {i+1} (%): "))
        except ValueError:
            print(" Ingresa solo números")
            continue
        
        if 65 <= lectura <= 85:
            suma += lectura
            contador += 1
        else:
            print("Lectura ignorada (outlier)")

    if contador > 0:
        promedio = suma / contador
        print("Promedio de lecturas válidas:", promedio)
    else:
        print("No hubo lecturas válidas")

    print("Fin del proceso")


if __name__ == "__main__":
    main()
