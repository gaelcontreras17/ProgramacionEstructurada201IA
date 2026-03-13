def demostracion():
    print("-- Ejemplos de match --")
    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            print("Opción 1 seleccionada")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}!")
        case "2":
            print("Opción 2 seleccionada")
            matricula = input("Ingrese su matrícula: ")
            print(f"Su matrícula es: {matricula}")
        case "3":
            print("Opción 3 seleccionada")
            semestre = input("Usted está en el semestre: ")
            print(f"Usted está en el semestre: {semestre}")
        case _:
            print("Opción no válida")