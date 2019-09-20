
vida_pikachu = 100
vida_combate = 0
dano_combate = 0
nombre_pokemon = 0
nombre_ataque = 0
X = 0


eligue_pokemon = int(input("Tu pokemon es Pikachu contra que Pokemon quieres luchar: 1 Charmander, 2 Squirtel, 3 Bulbasur :  "))

if eligue_pokemon == 1:
    dano_combate = 10
    vida_combate = 70
    nombre_pokemon = "Charmander"
    print("Has eleguido luchar contra Charmander")
    print()

elif eligue_pokemon == 2:
    dano_combate = 8
    vida_combate = 80
    nombre_pokemon = "Squirtel"
    print("Has eleguido luchar contra Squirtel")
    print()

elif eligue_pokemon == 3:
    dano_combate = 7
    vida_combate = 120
    nombre_pokemon = "Bulbasur"
    print("Has eleguido luchar contra Bulbasur")
    print()

while vida_combate >0 and vida_pikachu > 0:

    if X == 0:
        print("Empieza el Combate")
        print()
        X = 1

    eligue_ataque = int(input("Con que atacque quieres golpear: 1 Ataque Trueno, 2 Ataque Rapido :  "))

    if eligue_ataque == 1:
        vida_combate -= 12
        nombre_ataque = "Ataque Trueno"
    if eligue_ataque == 2:
        vida_combate -= 10
        nombre_ataque = "Ataque Rapido"

    print()
    print("Pikachu realiza {}".format(nombre_ataque))
    print()
    print("La vida de {} se reduce a {}".format(nombre_pokemon,vida_combate))
    print()
    vida_pikachu -= dano_combate
    print("{} ataca y reduce la vida de Pikachu a {} ".format(nombre_pokemon,vida_pikachu))
    print()

if vida_pikachu <= 0:
    print("Has perdido")
elif vida_combate <= 0:
    print("Has Ganado")

print("Termina el combate")

