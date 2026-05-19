# --- SISTEMA DE CONTROL BIOMÉTRICO ---
print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")

nombre = input("Nombre del Ingeniero: ")
id_empleado = int(input("ID de Empleado: "))
iris = input("¿El escaneo de Iris coincide? (si/no): ").lower()
facial = input("¿El reconocimiento facial es > 95%? (si/no): ").lower()

print()

# INTRUSO - ID inválido
if id_empleado <= 0:
    print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

# FALLO BIOMÉTRICO - uno o ambos escaneos fallan
elif iris == "no" or facial == "no":
    print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

# ACCESO TOTAL - Senior (ID < 100) y ambos escaneos correctos
elif id_empleado < 100 and iris == "si" and facial == "si":
    print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
    print(f"Generando log de entrada para el usuario: {id_empleado}...")

# ACCESO RESTRINGIDO - Junior (ID >= 100) y ambos escaneos correctos
elif id_empleado >= 100 and iris == "si" and facial == "si":
    print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
    print(f"Generando log de entrada para el usuario: {id_empleado}...")