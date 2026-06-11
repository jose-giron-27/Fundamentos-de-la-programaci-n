print("Le preguntamos al usuario sus datos") ## Se da 
nombre = input("¿Cual es tu nombre?: ") ## Nombre del usuario
edad = int(input("¿Cual es tu edad?: ")) ## Edad del usuario
print("Responda para la siguiente pregunta: 1 para si y 0 para no") ## Se dan los parametros para responder
boleto = int(input("¿Tiene boleto?: ")) ## Preguntamos al usuario si tiene boleto
puede_entrar = edad>= 18 and boleto == 1 ## Se establace que condición se tiene que dar para que sea true 
print("Hola: ", nombre, "¿Puede entrar? ", puede_entrar) #Se le dice al usuario que si puede entrar o no