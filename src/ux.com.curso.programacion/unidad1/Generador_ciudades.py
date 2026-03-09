from faker import Faker
fake = Faker ('es_MX')

ciudades_ia = []

#2. Operacion de llenado(ciclo)
for _ in range(5):
    ciudades_ia.append(fake.city())


#3. Escritura de arreglos (Mostrar resultados)
print("/n--DATATEST DE CIUDADES GENERADO--")
for i in range(len(ciudades_ia)):
    print(f"Registro{i+1}:{ciudades_ia[i]}")