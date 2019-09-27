
my_list = [14,12.2,True,"hola"]
tipo = ""
contador = 1
for valor in my_list:
    tipo = type(valor)
    print("El {} Valor vorsponde a {}".format(contador,tipo))
    contador += 1