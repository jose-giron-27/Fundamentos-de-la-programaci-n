print("Se le solicitarán los siguientes datos: ") ##Se piden los datos

n = int(input("¿Cuantos productos llevará? ")) ##Se pide el numero de productos

total = 0
precio_caro = 0

for i in range(n): ##Se establece la condicion
    producto = float(input(f"Cual es el precio del producto {i+1}? : ")) ##Se pide el precio de productos
    total = total + producto

if total >= 500: ##Condicion para total con descuento
    descuento = total*0.1
    Total_descuento = total-descuento
    print(f"El total de la compra es: Q{round(total,2)}" )
    print(f"Descuento aplicado: Q{round(descuento,2)}")
    print(f"Total a pagar: Q{round(Total_descuento,2)}")
else: ##Se establece la condicion sin descuento
    print(f"El total de la compra es: Q{round(total,2)}" )
    print(f"Total a pagar: Q{round(total,2)}")

if producto > precio_caro:
    precio_caro == producto



