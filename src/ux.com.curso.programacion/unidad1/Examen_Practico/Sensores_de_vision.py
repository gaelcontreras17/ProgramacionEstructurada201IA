def main():
    total_vram = 0
    limite = 2500

    print("Simulación de Entrenamiento por Lotes")
    print("Límite de VRAM:", limite, "MB")

    while True:
        try:
            lote = float(input("Ingresa el tamaño del lote (MB): "))
        except ValueError:
            print(" Ingresa solo números")
            continue
        
        total_vram += lote
        print("VRAM acumulada:", total_vram, "MB")
        
        if total_vram > limite:
            print(" Límite superado. Deteniendo carga (OOM).")
            break

    print("Fin del proceso")


if __name__ == "__main__":
    main()