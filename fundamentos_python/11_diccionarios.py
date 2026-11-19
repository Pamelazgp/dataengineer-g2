users=[
    ["Juan", 25,"m", "juan@email.com"],
    ["María", 30,"f", "maria@email.com"],
    ["Pedro", 35,"m", "pedro@email.com"],
    ["Lucía", 28,"f", "lucia@email.com"]
]

user_format={
    "id": 1,
    "name": "Juan",
    "age": 25,
    "gender": "m",
    "email": "juan@email.com"
}
new_users=[]
i=1

for user in users:
    user_dict={
        "id": i,
        "name": user[0],
        "age": user[1],
        "gender": user[2],
        "email": user[3]
    }
    
    i += 1
    new_users.append(user_dict)
print(new_users)

vehiculo={
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

"""modificar y agregar elementos a un diccionario"""
vehiculo["marca"] = "Honda"  # Modificar el valor de la clave "marca"
vehiculo["color"] = "Rojo"  # Agregar una nueva clave "color" con su valor correspondiente
print(vehiculo)  # Imprimir el diccionario actualizado

"""eliminar elementos de un diccionario"""
del vehiculo["color"]
vehiculo.pop("año")  # Eliminar la clave "año" y su valor correspondiente
print(vehiculo)  # Imprimir el diccionario actualizado después de eliminar 

"""metodos utiles de los diccionarios"""
print(vehiculo.keys())  # Imprimir las claves del diccionario
print(vehiculo.values())  # Imprimir los valores del diccionario    
print(vehiculo.items())  # Imprimir los pares clave-valor del diccionario

"""iterar sobre un diccionario"""
for clave in vehiculo:
    print(clave, vehiculo[clave])  # Imprimir cada clave y su valor 

for clave, valor in vehiculo.items():
    print(clave, valor)  # Imprimir cada clave y su valor usando items()        
    