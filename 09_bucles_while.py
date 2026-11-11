from time import sleep
lista=["python","rust", "java","c++","typeScript"]
tupla=("Ruby","go","c#","rust","javascript") #no puede mutar

contador=0
while contador<10:
   contador=contador+1
   #sleep(1) #pausa de 1 segundo
   print(contador)
else:
   print("El bucle ha terminado correctamente :snake:") #se ejecuta cuando el bucle termina correctamente

"""Salir de un bucle while con break"""

#while True:
#    print(contador)
#    contador+=1
#    if contador==15:
#        break # salir del bucle while cuando contador sea igual a 

""" Saltar una iteración con continue"""
# while True:
#     contador+=1
#     if contador==5:
#         continue # saltar la iteración cuando contador sea igual a 5
#     print(contador)
    
#     if contador==10:
#         break
     