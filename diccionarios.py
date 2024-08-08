#Ejercicios de Dictionary Comprehension 1

diccionario = {}

for i in range(1,11):
    diccionario[i] = i * 2

print(diccionario)

diccionario2 = {i: i * 2 for i in range(1,5)}
print(diccionario2)

import random
paises = ["México", "Argentina", "Colombia"]
poblacion = {}
for pais in paises:
    poblacion[pais] = random.randint(1,100)

print(poblacion)

poblacion2 = {pais: random.randint(1,100) for pais in paises}
print(poblacion2)

nombres = ["Nicolas", "Freddy", "Eddy"]
edades = [13, 19, 23]

print(list(zip(nombres, edades)))

diccionario_nuevo = {nombres : edades for (nombres, edades) in zip(nombres, edades)}
print(diccionario_nuevo)
