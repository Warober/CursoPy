
my_list = []
inpunt_user = ""
X=0



while inpunt_user != "Fin" :
    inpunt_user = input("Introduce los elementos para añadir a la listade la compra: (Teclea Fin para Salir)")
    if inpunt_user != "FiN" :
        my_list.append(inpunt_user)

longitud = len(my_list)


while longitud > X :
    print(my_list[X])
    X += 1


