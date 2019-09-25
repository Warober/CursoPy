
numero_tabla = int(input("Introduce el numero del cual quieres sacar la tabla:  "))
numero_min = int(input("Introduce el numero desde el cual quieres empezar:  "))
numero_max = int(input("Introduce el numero desde el cual quieres terminar:  "))
longitud = range(numero_min,numero_max + 1)
for numero in longitud:
    numero_invertido = len(longitud) - numero + 1
    print("{} * {} = {}".format(numero_tabla,numero_invertido, numero_invertido*numero_tabla ))

