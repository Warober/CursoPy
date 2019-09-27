
valor = 0
list_user = []
longitud = 0
media = 0
total = 0
suma = 0


while  valor != "FIN":
    valor = input("Introduce los numero para hcer la media (teclea FIN para terminar):  ")
    if  valor.isdigit():
        if valor != "FIN":
            valor = int(valor)
            list_user.append(valor)
    else:
        if valor != "FIN":
            print("introduce un valor numerico o FIN para Salir")

for numero_suma in list_user:
    suma = numero_suma
    total = total + suma

for numero in list_user:
    longitud += 1
media = total/longitud

print("La media de los numero introducidos son:   {}".format(media))
print("Los numeros intrducidos son:   {}".format(list_user))