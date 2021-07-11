import os

def clear():
    if os.name in ("ce", "nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")

def mostrarTablero(posiciones):
    print (f""" {posiciones[0]} | {posiciones[1]} | {posiciones[2]}
-----------
 {posiciones[3]} | {posiciones[4]} | {posiciones[5]}
-----------
 {posiciones[6]} | {posiciones[7]} | {posiciones[8]}""")

def jugadasGanadoras(posiciones):
    jugadaUno = [posiciones[0] == posiciones[1] == posiciones[2], posiciones[0]]
    jugadaDos = [posiciones[0] == posiciones[3] == posiciones[6], posiciones[0]]
    jugadaTres = [posiciones[0] == posiciones[4] == posiciones[8], posiciones[0]]
    jugadaCuatro = [posiciones[1] == posiciones[4] == posiciones[7], posiciones[1]]
    jugadaCinco = [posiciones[2] == posiciones[5] == posiciones[8], posiciones[2]]
    jugadaSeis = [posiciones[2] == posiciones[4] == posiciones[6], posiciones[2]]
    jugadaSiete = [posiciones[3] == posiciones[4] == posiciones[5], posiciones[3]]
    jugadaOcho = [posiciones[6] == posiciones[7] == posiciones[8], posiciones[6]]
    jugadas = (jugadaUno, jugadaDos, jugadaTres, jugadaCuatro, jugadaCinco, jugadaSeis, jugadaSiete, jugadaOcho)

    for jugada in jugadas:
        if jugada[0]:
            return jugada[1]
        else:
            continue
    return False

while True:
    posiciones = list(i for i in range(1,10))
    posicionesVacias = list(" " for i in range (1,10))
    turnoDe = True

    while True:
        clear()
        mostrarTablero(posiciones)

        if turnoDe:
            print ("Turno del jugador X.")
        else:
            print ("Turno del jugador O.")

        print ("Ingresá una posición valida.")
        entrada = input(">>> ")
        try:
            posicion = int(entrada) - 1
        except ValueError:
            continue
        if posiciones[posicion] in ("X", "O"):
            continue

        if turnoDe:
            posicionesVacias[posicion] = "X"
            posiciones[posicion] = "X"
        else:
            posicionesVacias[posicion] = "O"
            posiciones[posicion] = "O"

        turnoDe = not turnoDe

        ganador = jugadasGanadoras(posiciones)
        if ganador:
            clear()
            mostrarTablero(posicionesVacias)
            print("Ganó el jugador {}.".format(ganador))
            break

    print ("Desea continuar?")
    print ("\"Si\" para continuar, o cualquier otra cosa para salir.")
    continuar = input(">>> ")
    if continuar in ("SI", "Si", "si"):
        continue
    else:
        break

exit()
