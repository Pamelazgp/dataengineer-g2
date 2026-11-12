"""definicion de funciones"""
def saludar():
    print("Hola")

"""llamado a la funcion"""
saludar()  # Llamado a la función         

"""funcion con parametros"""         
def sumar (a,b):
    return a+b
"""llamado a la funcion"""
resultado = sumar(5,3)
print(resultado)

"""funcion con parametros y valores por defecto"""
def saludar_persona(nombre="Invitado"):
    print(f"Hola, {nombre}")

saludar_persona()
saludar_persona("Alice")

"""Funciones con numero variable de argumentos"""
"""*args permite pasar un número variable de argumentos posicionales a una función."""
def mostrar_numeros(*args):
    #args: (1, 2, 3, 4, 5)
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3, 4, 5)

"""**kwargs permite pasar un número variable de argumentos con nombre (clave-valor) a una función."""
def mostrar_informacion(**kwargs):
    #kwargs: {"nombre": "Eduardo", "edad": 30}
    for clave in kwargs:
        print(clave, kwargs[clave])

mostrar_informacion(nombre="Eduardo", edad=30)
