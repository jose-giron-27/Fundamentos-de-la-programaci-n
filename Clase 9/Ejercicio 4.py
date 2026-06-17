import random 
seguir = True
while seguir: 
    resultado = random.choice(["Cara", "Escudo"])
    print(f"Salió: {resultado}")
    pregunta = input("¿otra? (s/n)")
    if pregunta == "n":
        seguir = False

