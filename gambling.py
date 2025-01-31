from random import *

namep1 = input("Ingrese el mombre del primer jugador: ")
namep2 = input("ingrese el nombre del segundo jugador: ")

gamewinp1 = 0
gamewinp2 = 0

numgame = 1

continueGame = True

while (gamewinp1 < 2 or gamewinp2 < 2) and continueGame:
    print(f"Partida n°{numgame}")

    objetivo = randint(1,6)

    print("el objetivo es: ", objetivo)

    num1p1 = randint(1,6)
    num2p1 = randint(1,6)
    sumap1 = num1p1 + num2p1

    num1p2 = randint(1,6)
    num2p2 = randint(1,6)
    sumap2 = num1p2 + num2p2

    print(f"El jugador {namep1} ha sacado{num1p1} y {num2p1}")
    print(f"El jugador {namep2} ha sacado{num1p2} y {num2p2}")

    numwinners = 0
    if sumap1 == objetivo:
        numwinners += 1
        gamewinp1 += 1

    if sumap2 == objetivo:
        numwinners += 1
        gamewinp2 += 1

    if numwinners == 2:
        print("!Han ganado los 2!")
    elif numwinners == 1:
        if sumap1 == objetivo:
            print(f"Ha ganado el jugador {namep1}")
        if sumap2 == objetivo:
            print(f"Ha ganado el jugador {namep2}")

    continueGame = input("¿Quieres seguir jugando? {S/N}") == "S"

    numgame += 1

print("Juego terminado.")
print(f"Se han jugado un total de {numgame} veces")

if gamewinp1 == 2:
    print(f"Gana {namep1}")
if gamewinp2 == 2:
    print(f"Gana {namep2}")