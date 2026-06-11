print("Te solicitaremos los siguientes datos para que clasifiquemos tu triángulo") #introducción
lado_a = int(input("Lado a: ")) #solicita el lado a
lado_b = int(input("Lado b: ")) #solicita el lado b
lado_c = int(input("Lado c: ")) #solocita el lado c
if lado_a == lado_b and lado_b == lado_c: #condición cuando tiene 3 lados iguales
    print("Es un triángulo equilatero") #devuelve la respuesta si cumple con la condición
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c: #condición cuando tiene 2 lados iguales
    print("Es un triángulo isósceles") #devuelve la respuesta si cumple con la condición
else: #Condición si ninguno de los lados es igual
    print("Es un triángulo Escaleno") #devuelve la respuesta si cumple con la condición
print("Gracias por participar. ") #Agradecimiento