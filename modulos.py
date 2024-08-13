#Módulo para ver la ruta del sistema donde se está ejecutando el archivo
import sys
print(sys.path)

#Módulo para buscar dígitos y carácteres dentro de un string
import re

text = "Mi número de télefono es 311 123 121, el código del país es 57, mi número de la suerte es el 3"

result = re.findall("[0-9]+", text)
print(result)

#Módulo para obtener el tiempo del ordenador, también para hacerlo con formato
import time

timestamp = time.time()
print(timestamp)

local = time.localtime()
result2 = time.asctime(local)

print(result2)

#Módulo para saber la frecuencia de un valor dentro de una lista
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]

counter = collections.Counter(numbers)
print(counter)