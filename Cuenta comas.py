
frase_usuario = input("Escriba la frases para contar los espacios y signos de puntuacion:  ")

punto = "."
punto_coma = ";"
coma = ","
espacios = " "
espacios_cuenta = 0
punto_cuentas = 0
punto_coma_cuentas = 0
coma_cuenta = 0

for lestras in frase_usuario:
    if lestras in punto:
        punto_cuentas += 1
    elif lestras == espacios:
        espacios_cuenta += 1
    elif lestras == punto_coma:
        punto_coma_cuentas += 1
    elif lestras == coma:
        coma_cuenta += 1

print("Tu frase tiene {} Espacios {} Puntos  {} Punto y comas {} Comas ".format(espacios_cuenta,punto_cuentas, punto_coma_cuentas,coma_cuenta))



