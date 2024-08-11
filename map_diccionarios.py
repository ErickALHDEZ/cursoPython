#Estos es una lista de diccionarios
items = [
    {
        "producto": "camisa",
        "precio" : 100,
    },
    {
        "producto": "pantalon",
        "precio": 300
    },
        {
        "producto": "pantalon 2",
        "precio": 200
    }
]

#Creamos una lista de solo los precios utilizando un map y una función anonima lambda
precios = list(map(lambda item: item["precio"], items))
print(precios)

#Declaro una función en la cual recibio item, que es el nombre de mi diccionario
def agregar_impuestos(item):
    item["impuestos"] = item["precio"] * .19
    #regreso el item con el elemento nuevo de impuestos
    return item

new_items = list(map(agregar_impuestos, items))
print(new_items)