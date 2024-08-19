#En este código capturamos dentro del bloque try todos los posibles casos en los que se puede
#dar un error y ponemos los except individuales para cada caso, al ejecutar el programa nosotros
#Solo vamos a ver el primer error de division by zero por que al detectar un solo error, ya no va
#a proceder con el resto del try, pero si va a imprimir el "Hola" al final ya que no detiene el
#programa, solo el bloque dentro del try.

try:
    print( 0/0)
    assert 1!=1, "Uno no es igual a uno"
    age = 10
    if age < 18:
        raise Exception("No se permiten menores de edad")
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print("Hola")