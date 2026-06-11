##Sistema de acceso para una persona que si tiene más de 18 años puede ingresar, si tiene entre 15 y 17 años puede ingresar. 
##Si es mayor de 18 años puede ingresar. 

edad = int(input("Ingresar porfa tu edad: ")) ##Esto es una variable con un int input para que el usuario ingrese su edad
nombre = input("¿Como te llamas?: ") ##Esto es una variable con un input para que el usuario ingrese su nombre

if edad <= 18: ## esto es una condicional if para verificar si la edad es mayor o igual a 18 años 
    print("Hola :)"), nombre + ",", "Puedes enrtar al establecimiento" ##Esto se va a ejecutar media vez la persona sea mayor de 18 años
elif edad >= 15 and edad <18: ##Esto es una condicional elif para que la persona pueda entrar con sus papas o con un adulto. 
    print("Hola: "), nombre + ",", "Puedes entrar al establecimiento PERO acompañado por un adulto" ##Esto se va a ejecutar media vez la persona
else: ## Esto es una condicional else para que la persona no pueda entrar al establecimiento
    print("Hola: ", nombre + ",", "lo lamento much :( no puedes entrar al establecimiento)"  )    
