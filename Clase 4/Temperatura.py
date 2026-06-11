# Ejercicio que mide temp y da una recomendación

temperatura = float(input("Ingresa la temperatura en grados celcius: "))

if temperatura > 30 and temperatura < 45:
    print("Hace calor, toma agua")
elif temperatura >= 15 and temperatura <= 30:
    print("Clima agradable")
elif temperatura < 15 and temperatura > 0:
    print("Hace frío. Abrígate")
else: 
    print("Revisa si los datos del clima son correctos")

print("Temperatura registrada: ", temperatura,"C")




