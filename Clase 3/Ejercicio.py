nombre = input("¿Cual es tu nombre?: ")
edad = int(input("¿Cual es tu edad?: "))
anio_actual = 2026
fecha_de_nacimiento = anio_actual - edad
adulto = edad >= 18
print ("Hola! ", nombre, "Naciste en: ", fecha_de_nacimiento, "¿Eres mayor de edad? ", adulto)
