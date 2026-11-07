lista=["python","rust", "java","c++","typeScript"]

""" Recorrer una lista"""
for lenguaje in lista:
    print(lenguaje) #output python rust java c++ typeScript

""" Recorrer cadenas de texto """
texto="I love python"
for letra in texto:
    print(letra) #output I l o v e p y t h o n     

""" Recorrer una lista con un índice """
for index, lenguaje in enumerate(lista):
    print(index, lenguaje) 
    