import random

jugador = input("Elige piedra, papel o tijera: ")
bot = random.choice(["piedra", "papel", "tijera"])
print("El bot escoge: ", bot)

if jugador == bot:
    print("Empate ⚔️")

elif jugador == "piedra" and bot == "papel":
    print("Gana papel 📄")

elif jugador == "piedra" and bot == "tijera":
    print("Gana piedra 🪨")

elif jugador == "papel" and bot == "tijera":
    print("Gana tijera ✂️")

elif bot == "piedra" and jugador == "papel":
    print("Gana papel 📄")

elif bot == "piedra" and jugador == "tijera":
    print("Gana piedra 🪨")

elif bot == "papel" and jugador == "tijera":
    print("Gana tijera ✂️")


