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
    
camioneta=Vehiculo("Toyota", "Blanco", "Hilux")
print(camioneta.color)

coche = Vehiculo("VM", "Negro", "Golf")
print(coche.color)