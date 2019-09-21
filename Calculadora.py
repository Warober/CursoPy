operacion_input = int(input("Que operacion quieres realizar: 1 Sumar, 2 Resta, 3 Multiplicacion, 4 Division:  "))
primer_numero = int(input("Introduce el Primer numero: "))
segundo_numero = int(input("Introduce el Segundo numero: "))
signo = 0

if operacion_input == 1:
   resultado = primer_numero + segundo_numero
   signo = "+"
elif operacion_input == 2:
    resultado = primer_numero - segundo_numero
    signo = "-"
elif operacion_input == 3:
    resultado = primer_numero * segundo_numero
    signo = "X"
elif operacion_input == 4:
    resultado = primer_numero / segundo_numero
    signo = "/"

print("El resultado de {} {} {} es de = {}".format(primer_numero,signo,segundo_numero,resultado))

