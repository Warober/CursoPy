
numero_tabla = int(input("Introduce el numero del cual quieres sacar la tabla:  "))
numero_min = int(input("Introduce el numero desde el cual quieres empezar:  "))
numero_max = int(input("Introduce el numero desde el cual quieres terminar:  "))

for numero in range(numero_min,numero_max+1):
    print("{} * {} = {}".format(numero_tabla,numero, numero*numero_tabla ))