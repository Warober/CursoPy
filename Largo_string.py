

my_list = ["roberto","lol","True","hola"]
Largo = 0
contador = 1
tipo = ""

for valor in my_list:
    Largo = len(valor)
    tipo = type(valor)
    print("El {} Valor tiene una longitud de {} y es una {}".format(contador,Largo,tipo))
    contador += 1