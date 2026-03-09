#importar la libreria faker
from faker import Faker 

faker = Faker ("es_MX")

print("generando Datos Dummy con faker")

print (f"Nombre:  {faker.name()}")
print (f"Direccion:  {faker.address}")
print(f"Telefono:  {faker.phone_number()}")
print(f"Correo:  {faker.email()}")