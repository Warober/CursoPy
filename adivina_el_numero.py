
numero_a_adivinar = int(input("Teclea un numero del 1 al 10 el cual tendran que  adivinar:  "))


x = 0
while x== 0:
    numero_usuario = int(input("Adivina el numero tecleado con anterioridad el rango es del 1 al 10:  "))
    if numero_a_adivinar == numero_usuario :
        print("Has Ganado")
        x = 1
    else:
        print("Prueba otra vez")
