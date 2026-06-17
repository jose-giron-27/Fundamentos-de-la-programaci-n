saldo = 1000
seguir = True
while seguir:
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("¿Qué opción quieres? ") 

    if opcion == "1":
        print(f"Tu saldo es: {saldo}")


    elif opcion == "2":
        monto = float(input("¿Qué monto quieres depositar? "))
        saldo = saldo + monto
        print(f"Tu nuevo saldo es: {saldo}")    
    
    elif opcion == "3":
        monto = float(input("¿Qué monto quieres retirar? "))
        if monto <= saldo:
            saldo = saldo - monto
        else:
            print("No tienes suficiente saldo")
        print(f"Tu nuevo saldo es: {saldo}")

    elif opcion == "4":
        seguir = False
    else:
        print("Opción no válida")

print("Hasta luego")
    


    



   
   