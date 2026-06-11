import random
aleatorio = random.randint(1,5)

usuario = int(input("Ingresa el numero que cree es el correcto "))

if usuario > aleatorio:
    print("El numero que escogiste es mayor, el numero era: ", aleatorio)

elif usuario < aleatorio:
    print("El numero que escogiste es menor, el numero era: ", aleatorio)

elif usuario == aleatorio:
    print("¡¡Ganaste brooo!!"," ", " El número era: ", aleatorio)