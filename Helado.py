

X=False

while X == False:
    apetece_helado = input("¿Te apetece un helado?     (Si / No)      :").upper()
    if apetece_helado == "SI":
        X = True
    elif apetece_helado == "NO":
        X = True
    else:
        print("No se que has escrito vuelve a probar")

if apetece_helado == "NO":
    print("     Vuelve cuando te apetezca    ")
else:
    X=False
    while X == False:
        tienes_dinero = input("¿Tienes dinero?    (Si / No):      ").upper()
        if tienes_dinero == "SI":
            X = True
            print("Aqui tienes tu helado")
        elif tienes_dinero == "NO":
            esta_tu_tia = input("¿Esta tu tia?      (Si / No):      ").upper()
            if esta_tu_tia == "SI":
                print("Aqui tienes tu helado")
                X = True
            elif esta_tu_tia == "NO":
                print("     Vuelve cuando tengas dinero o te invite tu tia    ")
                X = True
            else:
                print("No se que has escrito vuelve a probar")
        else:
            print("No se que has escrito vuelve a probar")














