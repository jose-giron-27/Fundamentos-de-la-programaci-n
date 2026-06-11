print("Bienvenido, vamos a jugar en juego :)") ##Introduccion
print("Tienes que adivinar que adivinar un número del 1 al 100") ##Reglas
print("No te preocupes yo te guiaré en el proceso")

secreto = 67 ##Numero secreto
intento = int(input("¿Que numero crees que es?: ")) ##Solicitud de numero

if intento == secreto: ##Condicional cuando es correcto
    print("Perfecto, eres un suertudo") ##Mensaje del resultado
elif intento > secreto:
    print("Demasiado alto, intenta con un número más bajo. Te daré una pista") ##Condicional cuando es incorrecto
    operacion = abs(secreto-intento) ##Aritmética para calcular la diferencia con absolut
    hint = (operacion*100)/secreto ##Aritmética para calcular hint
    print("Estas a un ", round(hint,2),"%","de la respuesta", ". La diferencia de tu respuesta es: ", operacion) ##Entregar la pista

elif intento < secreto:
    print("Demasiado bajo, intenta con un número más alto. Te daré una pista") ##Condicional cuando es incorrecto
    operacion = abs(secreto-intento) ##Aritmética para calcular la diferencia con absolut
    hint = (operacion*100)/secreto ##Aritmética para calcular hint
    print("Estas a un ", round(hint,2),"%","de la respuesta", ". La diferencia de tu respuesta es: ", operacion) ##Entregar la pista

print("Tu intento: ", intento) ## Mensaje mencionando el intento realizado 
    
