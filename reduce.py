import functools

numbers = [1,2,3,4]

#Una función declarada que realiza lo mismo que la lambda de aquí abajo
def acumulador(counter, item):
    print("contador:  ", counter)
    print("item:  ", item)
    return counter + item

result = functools.reduce(acumulador, numbers )
#Función lambda con la cual sumo los valores dentro de la lista de numbers
#result = functools.reduce(lambda counter, item: counter + item, numbers )

print(result)

