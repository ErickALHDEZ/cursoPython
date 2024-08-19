import csv

def read_csv(path):
    # Abrir el archivo CSV
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        # Convertir filas en una lista de listas
        filas = list(reader)
        # Transponer filas a columnas
        columnas = list(zip(*filas))

        #Aquí después de acomodar, sumamos el total
        columna_numeros = columnas[1]
        total = sum(int(num) for num in columna_numeros)

    return total

response = read_csv('./data.csv')
print(response)