"""1. Validar que una contraseña tenga al menos 8 caracteres"""
# Input: "1234567"
#output: "introduce minimo 8 caracteres"
#input: "12345678"
#output: "contraseña valida"


#resuelto por Pamela
#input_contraseña=input("Introduce una contraseña: ")
# while len(input_contraseña)<8:
#     print("introduce minimo 8 caracteres")
#     break
# else:
#     print("contraseña valida")

"""2. Ingresar un número y crear una tabla de multiplicar hasta el 10"""
#input: 5
#output: 5 x 1 = 5, 5 x 2 = 10, 5 x 3 = 15, 5 x 4 = 20, 5 x 5 = 25, 5 x 6 = 30, 5 x 7 = 35, 5 x 8 = 40, 5 x 9 = 45, 5 x 10 = 50

# input_numero=int(input("Ingrese un número para crear su tabla de multiplicar: "))
# i=1
# while i<=10:
#     print(input_numero, "x", i, "=", input_numero*i, "\n")
#     i=i+1

#resuelto por el profesor

# while True:
#     password=input("Ingrese una contraseña: ")
#     if len(password)<8:
#         print("Introduce minimo 8 caracteres")
#     else:
#         print("Contraseña valida")
#         break

#ejrcicio 2

# while True:
#     number=int(input("Ingrese un número : "))
#     i=1
#     while i<=10:
#         print(f"{number} x {i} = {number*i}")
#         i+=1