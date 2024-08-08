#Ejercicios de Dictionary Comprehension 2

import random
paises = ["México", "Argentina", "Colombia"]

poblacion2 = {pais: random.randint(1,100) for pais in paises}
print(poblacion2)

#Aquí creo un nuevo diccionario
resultado = { pais: poblacion for (pais, poblacion) in poblacion2.items() if poblacion > 30}
print(resultado)

#Diccionario que regresa únicamente las vocales de mi texto
#y las transforma a mayúsculas

texto = "Hola soy Erick"
unico = { c: c.upper() for c in texto if c in "aeiou"}
print(unico)
