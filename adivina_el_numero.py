
numero_a_adivinar = 10

numero_usuario = int(input("Teclea un numero del 1 al 10 para adivinar el numero pensado:  "))

if numero_a_adivinar == numero_usuario:
    print("Has Ganado")

else:
    print("Has perdido")