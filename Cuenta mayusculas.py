frase_usuario = input("Escriba la frases para contar las mayusculas:  ")

mayusculas = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
mayusculas_cuenta = 0

for lestras in frase_usuario:
    if lestras in mayusculas:
        mayusculas_cuenta += 1

print("Tu frase tiene {} Mayusculas ".format(mayusculas_cuenta))
