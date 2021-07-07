import os
def mostrarTablero(posiciones):
    tablero = ( f""" {posiciones[0]} | {posiciones[1]} | {posiciones[2]}
-----------
 {posiciones[3]} | {posiciones[4]} | {posiciones[5]}
-----------
 {posiciones[6]} | {posiciones[7]} | {posiciones[8]}""")
    return tablero
posiciones = list(i for i in range(1,10))
turnoDe = True
#posiciones[6], posiciones [7], posiciones[8] = "X", "X", "X"
#mostrarTablero(posiciones)

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
    for i in range(0,8):
        if (jugadas[i])[0]:
            return (jugadas[i])[1]
        else:
            continue
        return False

while True:
    while True:
        try:
            print (mostrarTablero(posiciones), "\nIngresá una posición valida.")
            posicion = int(input(">>> ")) - 1
        except:
            pass

        posiciones[posicion] = "X" if turnoDe else "O"
        turnoDe = not turnoDe
        print(mostrarTablero(posiciones))
        os.system("cls")

        ganador = jugadasGanadoras(posiciones)
        if ganador:
             print("\nGanó el jugador {}.".format(ganador))
             break
    continuar = input(r"Desea continuar?\n"Si" para continuar, o cualquier otra cosa para salir.")
    if continuar == "s" or continuar == "S":
        break
