
valor = 0
list_user = []
longitud = 0

while  valor != "FIN":
    valor = input("Introduce los numero para contar (teclea FIN para terminar):  ")
    if  valor.isdigit():
        if valor != "FIN":
            valor = int(valor)
            list_user.append(valor)
    else:
        if valor != "FIN":
            print("introduce un valor numerico o FIN para Salir")



for numero in list_user:
    longitud += 1

print("La cantidad de numero introducida son:   {}".format(longitud))
print("Los numeros intrducidos son:   {}".format(list_user))