print("Hola usuario, te pediremos los siguientes datos") ## Introducción
print("Los tipos de clientes son los siguientes: VIP, Estudiante, Regular, otros")##Tipos de clientes
tipo = input("¿Que tipo de cliente eres?: ")##Solicitud de tipo de usuario
monto = float(input("¿Cual fue el monto de tu compra?: "))##Solicitud de tipo de compra

if tipo == "VIP": ##Condicional VIP
    descuento = monto*0.20 ##Operacion de descuento
    print("Tu descuento es del 20%")
elif tipo == "Estudiante": ##Condicional Estudiante
    descuento = monto*0.15 ##Operacion de descuento
    print("Tu descuento es del 15%")
elif tipo == "Regular": ##Condicional Regular
    descuento = monto*0.05 ##Operacion de descuento
    print("Tu descuento es del 5%")
else: 
    descuento = 0
    print("No tienes descuento")

total = monto-descuento ##Operacion de total a pagar
print("Total a pagar: Q", round(total,2)) ##Se muestra el total a pagar

