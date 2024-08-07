class Vehiculo:
    def __init__(self, marca, modelo, precio):
        #Encapsulamiento
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca}. ha sido vendido")
        else:
            print(f"El vehículo {self.marca}. no está disponible")

    #Abstracción
    def verifica_disponible(self):
        return self.disponible
    
    #Abstracción
    def obtener_precio(self):
        return self.precio
    
    def iniciar_motores(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def detener_motores(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

#Herencia       
class Coche(Vehiculo):
    #Polimorfismo
    def iniciar_motores(self):
        if not self.disponible:
            return f"El motor del coche {self.marca} está en marcha"
        else:
            return f"El coche de marca {self.marca} no está disponible"
    
    #Polimorfismo
    def detener_motores(self):
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido"
        else:
            return f"El coche {self.marca} no está disponible"
        
#Herencia
class Bicicleta(Vehiculo):
    #Polimorfismo
    def iniciar_motores(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} está en marcha"
        else:
            return f"La bicicleta {self.marca} no está disponible"

    #Polimorfismo
    def detener_motores(self):
        if self.disponible:
            return f"La bicicleta {self.marca} se ha detenido"
        else:
            return f"La bicicleta {self.marca} no está disponible"
        
class Camion(Vehiculo):
    def iniciar_motores(self):
        if not self.disponible:
            return f"El motor del camión {self.marca} está en marcha"
        else:
            return f"El camión de marca {self.marca} no está disponible"
        
    def detener_motores(self):
        if self.disponible:
            return f"El motor del camión {self.marca} se ha detenido"
        else:
            return f"El camión {self.marca} no está disponible"
        
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.verifica_disponible():
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f"Lo siento, {vehiculo.marca} no está disponible")

    def consultar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.verifica_disponible():
            disponibilidad = "Disponible"
        else:
            disponibilidad = "No Disponible"
        print(f"El {vehiculo.marca} está {disponibilidad} y cuesta {vehiculo.obtener_precio()}")

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_vehiculos(self, vehiculo:Vehiculo):
        self.inventario.append(vehiculo)
        print(f"El {vehiculo.marca} ha sido añadido al inventario")

    def registrar_clientes(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"El {cliente.nombre} ha sido añadido")

    def mostrar_vehiculos_disponibles(self):
        print("Vehiculos disponibles en la tienda:")
        for vehiculo in self.inventario:
            if vehiculo.verifica_disponible():
                print(f"- {vehiculo.marca} por {vehiculo.obtener_precio()}")


coche1 = Coche("Toyota", "Corolla", 2000)
bicicleta1 = Bicicleta("Yamaha", "MT-07", 700)
camion1 = Camion("Volvo", "FH16", 8000)

cliente1 = Cliente("Carlos")

concesionaria = Concesionaria()
concesionaria.añadir_vehiculos(coche1)
concesionaria.añadir_vehiculos(bicicleta1)
concesionaria.añadir_vehiculos(camion1)

#Mostrar vehículos disponibles
concesionaria.mostrar_vehiculos_disponibles()

#El cliente va a consultar un vehículo
cliente1.consultar_vehiculo(coche1)

#El cliente va a comprar un vehículo
cliente1.comprar_vehiculo(coche1)

#Mostrar vehículos disponibles
concesionaria.mostrar_vehiculos_disponibles()