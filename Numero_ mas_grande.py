
my_lista = []
numero_grande = 0
numero = input("Introduce 10 numeros y te dire el mas grande: ")

while len(my_lista) < 10:

    while not numero.isdigit():
        print("Has introducido un valor que no es numerico  ")
        numero = (input("Introduce un numero: "))
    my_lista.append(int(numero))
    print("Numero añadido")
    numero = (input("Introduce un numero: "))

for grande in my_lista:
    if grande > numero_grande:
        numero_grande = grande

print("El numero mas grande es:  {} de estos numero {}".format(numero_grande,my_lista))

