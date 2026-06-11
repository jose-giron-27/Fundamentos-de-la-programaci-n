import random 

print("Se le solicitarán los siguientes datos: ") ##Se piden los datos
n = int(input("Elige el numero de tiros que deseas realizar: ")) ##Se pide numero de veces 

suma = 0

for i in range(n): ##Se define ciclo for
    tiro = random.randint(1,6) ##Se define random para generar los tiros
    suma = suma + tiro ##Se define suma de tiros
    print(f"Tiro {i+1}: {tiro}")
print(f"Suma total: {suma}") 
Promedio = suma/n ##Se define el promedio
print(f"Promedio: {round(Promedio,2)}")

if Promedio > 3.5: ##Se define condicional para mensaje
    print("Buena racha")
else: 
    print("Vas bien sigue asi!")
