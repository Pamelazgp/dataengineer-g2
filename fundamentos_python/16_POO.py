""" Las clases nos permiten implementar el paradigma de Programación 
orientada a Objetos (POO). Nos permite crear tipos de datos, encapsular
atributos y comportamientos, y organizar código de forma modular y reutilizable"""

class Persona:
    pass

class Vehiculo:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        #encapsulacion
        self.__codigo="VW0001"
        
    def ver_datos(self):
       # self.marca="se cambió la marca"
        print(f"Este vehiculo es de la marca {self.marca}, color {self.color} y modelo {self.modelo} y código {self.__codigo}")
    
    #Encapsulación
    def __informacion_privada(self):
        print(f"esta informacion es privada: {self.__codigo}")
    
camioneta=Vehiculo("Toyota", "Blanco", "Hilux")
# print(camioneta.color)

coche = Vehiculo("VM", "Negro", "Golf")
# print(coche.color)
# coche.ver_datos()
# print(coche.__codigo)
# coche.__informacion_privada()

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def saltar(self):
        print(f"{self.nombre} ha saltado")
        
    @staticmethod
    def vacunas(mensaje):
        print(mensaje)    
        
# Herencia: permite crear clases derivadas que heredan atributos y métodos      
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice Miau!")

perro=Animal("Rex")
perro.saltar()
perro.vacunas("Las vacunas estan al dia")

pelusa=Gato("pelusa")
pelusa.hablar()
pelusa.saltar()