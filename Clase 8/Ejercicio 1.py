print("Se le solicitará el siguiente dato al usuario")
num = int(input("Ingresa tu número: ")) ## Se solicita el numero al usuario

for i in range(1,11): ## Se ingresa el ciclo for para la multiplicación
    multi = num*i ## Se declara la variable que almacenará la multiplicación
    
    if multi%2 == 0: ## Condicional para mayor a 30
        print(f"{num} x {i} = {multi} <- Par")
    else:
        print(f"{num} x {i} = {multi}")