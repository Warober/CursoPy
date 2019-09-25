frase_usuario = input("Escriba la frases para contar las mayusculas:  ")

vocales = "a","e","i","o","u"
vocales_cuenta = []

for letras in frase_usuario:
    if letras in vocales:
        vocales_cuenta.append(letras)


print("Tu frase tiene estas vocales {} ".format(vocales_cuenta))