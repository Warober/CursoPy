
my_list = []
inpunt_user = ""

while inpunt_user != "Fin" :
    inpunt_user = input("Introduce los elementos para añadir a la listade la compra: (Teclea Fin para Salir)")
    if inpunt_user != "FiN" :
        my_list.append(inpunt_user)

for X in my_list:
    print("Tengo que comprar {}".format(my_list))





