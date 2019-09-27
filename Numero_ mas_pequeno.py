
my_lista = []
numero_pequeno = 0
numero = input("Introduce 10 numeros y te dire el mas pequeño: ")

while len(my_lista) < 10:

    while not numero.isdigit():
        print("Has introducido un valor que no es numerico  ")
        numero = (input("Introduce un numero: "))
    my_lista.append(int(numero))
    print("Numero añadido")
    numero = (input("Introduce un numero: "))

for pequeno in my_lista:
    numero_pequeno = my_lista[0]
    if pequeno < numero_pequeno:
        numero_pequeno = pequeno

print("El numero mas pequeño es:  {} de estos numero {}".format(numero_pequeno,my_lista))

