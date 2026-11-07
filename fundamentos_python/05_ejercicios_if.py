#Determinar el mayor de dos números

numero1= int(input("Ingrese el primer número: "))
numero2= int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El mayor es:", numero1)
elif numero2 > numero1:
    print("El mayor es:", numero2)
else:
    print("Los números son iguales")