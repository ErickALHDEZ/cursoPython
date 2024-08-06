#Creamos la clase Auto

class Auto:
    #Creamos el constructor
    def __init__(self, marca, modelo, precio):
        #Definimos los parámetros
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock_tienda = True

    #Definimos la función de compra venta
    def vender(self):
        if self.stock_tienda:
            self.stock_tienda = False
            print(f"El auto {self.marca} {self.modelo} se ha vendido")
        else:
            print(f"El auto {self.marca} {self.modelo} no se encuentra disponible para su venta")

    def comprar(self):
            self.stock_tienda = True
            print(f"El auto {self.marca} {self.modelo} se ha comprado")

#Creo la clase Usuario, que es el vendedor de la concesionaria de autos
class Usuario:
    #Definimos el constructor
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.autos_vendidos = []

    #Definimos la función para vender un auto
    def vender_auto(self, auto):
        if auto.stock_tienda:
            auto.vender()
            self.autos_vendidos.append(auto)
        else:
            print(f"""El auto {self.marca} {self.modelo} 
            no se encuentra disponible para su venta""")
    
    #Definimos la función para comprar un auto
    def comprar_auto(self, auto):
        if auto.stock_tienda == False:
            auto.comprar()
            self.autos_vendidos.remove(auto)
        else:
            print(f"""El auto {self.marca} {self.modelo} 
            no se encuentra disponible para su compra""")

#Creamos la clase concesionaria
class Concesionaria:
    #Creamos el constructor
    def __init__(self):
        self.autos = []
        self.usuarios = []
    
    #Definimos la función para añadir coches,
    #registrar usuarios y mostrar autos disponibles.

    def añadir_auto(self, auto):
        self.autos.append(auto)
        print(f"El auto {auto.marca} {auto.modelo}  ha sido agregado")

    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.nombre} ha sido registrado")

    def mostrar_autos_stock(self):
        print("Autos disponibles")
        for auto in self.autos:
            if auto.stock_tienda:
                print(f"{auto.marca} {auto.modelo}")

#Crear los autos
auto1 = Auto("Ford", "Focus", 700)
auto2 = Auto("Nissan", "Versa", 500)

#Crear usuario
usuario1 = Usuario("Erick", "001")

#Crear concesionaria
concesionaria = Concesionaria()
concesionaria.añadir_auto(auto1)
concesionaria.añadir_auto(auto2)
concesionaria.registrar_usuario(usuario1)

#Mostrar autos disponibles
concesionaria.mostrar_autos_stock()

#Un usuario lleva a cabo la venta
usuario1.vender_auto(auto1)

#Mostrar autos disponibles
concesionaria.mostrar_autos_stock()

#Un usuario lleva a cabo la compra
usuario1.comprar_auto(auto1)

#Mostrar autos disponibles
concesionaria.mostrar_autos_stock()

