with open("./texto.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("Nuevas cosas")