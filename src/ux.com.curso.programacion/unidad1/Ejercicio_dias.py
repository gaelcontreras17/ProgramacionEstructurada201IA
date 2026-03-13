def Dias():
    print("-- Dias --")
    opcion = input("ingrese una opcion (1-7):")

    match opcion:
        case "1":
            print("Lunes")
        case "2":
            print("Martes")
        case "3":
            print("Miercoles")
        case "4":
            print("Jueves")
        case "5":
            print("Viernes")
        case "6":
            print("Sabado")
        case "7":
            print("Domingo")
        case _:
            print ("opcion no valida") 

def main():
    Dias()
    
if __name__ == "__main__":
    main()