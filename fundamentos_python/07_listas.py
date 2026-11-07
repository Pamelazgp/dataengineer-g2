#son colecciones ordenadas y mutables de elementos, que permiten almacenar multiples elementos en una sola variable
lista1=[1,2,3,4,5]
lista2=["python","rust","typeScript"]  
lista3=[1,"a",True,3.14]

""" Acceder a los elementos de una lista """
print(lista2[1]) #output b
print(lista3[-1]) #output True  

""" slicing (rebanado) de listas """
print(lista1[1:4]) #output [2, 3, 4]
print(lista1[:3]) #output [1, 2, 3]
print(lista1[3:]) #output [4, 5]  
print(lista1[::2]) #output [1, 3, 5]
print(lista1[::-1]) #output [5, 4, 3, 2, 1]

""" Modificar elementos de una lista """
lista1[4] = 10
print(lista1) #output [1, 2, 3, 4, 10]

""" Agregar elementos a una lista """
lista1=lista1+[6,7]
print(lista1) #output [1, 2, 3, 4, 10, 6, 7]

""" Obtener la longitud de una lista """
print(len(lista1)) #output 7    

""" métodos de listas """
lista=["python"]
lista.append("go") #agrega un elemento al final de la lista
print(lista) #output ["python", "go"]

lista.insert(0,"java") #agrega un elemento en la posición indicada
print(lista) #output ["java", "python", "go"]   

lista.remove("go") #elimina el primer elemento que coincida con el valor indicado
print(lista) #output ["java", "python"]     

lista.pop(0) #elimina el elemento en la posición indicada, pero si no se indica posición elimina el último elemento
print(lista) #output ["python"] 

print(lista.index("python")) #devuelve la posición del primer elemento que coincida con el valor indicado  
#output 0

print(lista.count("python")) #devuelve el número de veces que aparece el valor indicado en la lista 
#output 1

lista2 = [5, 10, 2]
lista2.sort()
print(lista2)
# Output: [2, 5, 10]

lista2.reverse()
print(lista2)
# Output: [10, 5, 2]

lista2.clear()
print(lista2)
# Output: []  
