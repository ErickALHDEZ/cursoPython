file = open("./texto.txt")
#print(file.read())
#print(file.readline())

for line in file:
    print(line)

file.close()

with open("/.texto.txt") as file:
    for line in file:
        print(line)