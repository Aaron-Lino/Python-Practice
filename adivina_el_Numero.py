from random import *
nombre = input("Por favor introducir tu nombre: ")
intentos = 0
print(f"Hola {nombre} para este juego tienes 8 intentos para adivinar el numero del 1 al 100.")
print("Te deseo suerte")
numero_Programa = int(randint(1,100))
while intentos < 8:
    numero_elegido = int(input("Introduzca el numero: "))
    intentos += 1
    if numero_elegido not in range(1,101):
        print(f"El numero elegido esta fuera de rango")
        print(f"!tienes {intentos} intentos")

    elif numero_elegido > numero_Programa:
        print(f"!Te pasaste tu numero elegido fue {numero_elegido} !")
        print(f"!tienes {intentos} intentos")

    elif numero_elegido < numero_Programa:
        print(f"!Te falto tu numero elegido fue {numero_elegido}!")
        print(f"!tienes {intentos} intentos")

    elif numero_elegido == numero_Programa:
        print(f"Lo lograste pasaste y solo con {intentos} intentos")
        break

if intentos != numero_Programa:
    print(f"Exesite el numero de intentos, el numero secreo era {numero_Programa}")
