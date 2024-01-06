#Autor:  larrix14k
#Inicio 5 enero 2024 
#Fin 5 enero 2024 
#1. Create an online banking system with the following features:
#Users must be able to log in with a username and password.
#If the user enters the wrong credentials three times, the system must lock them out.
#The initial balance in the bank account is $2000.
#The system must allow users to deposit, withdraw, view, and transfer money.
#The system must display a menu for users to perform transactions" 
#######################################################################################
username = input("Ingrese su usuario:") #Ingresar el usuario
password = input("Ingrese su password:") #Ingresar la contraseña
if username == "antonio24" and password == "francia24": #Usuario y contraseña escogidos
    print("Bienvenido al sistema bancario") #Mensaje de Bienvenida
else:
    print("Credenciales incorrectas, tiene dos intentos")#Mensaje de Credenciales erroneas
    print("Ingrese su usuario")#Mensaje para ingresar usuario
    username = input()#Ingreso del usuario
    print("Ingrese su password")#Mensaje de ingreso de contraseña
    password = input()#Ingreso de contraseña
    if username == "antonio24" and password == "francia24":#Usuario y contraseña escogidos
        auth = True 
    else: 
        print("Credenciales incorrectas, tiene 1 intento")#Mensaje de credenciales erroneas
        print("Ingrese su usuario")#Mensaje para ingresar usuario
        username = input()#Ingreso del usuario
        print("Ingrese su password")#Mensaje de ingreso de contraseña
        password = input()#Ingreso de contraseña
        if username == "antonio24" and password == "francia24":
            auth = True 
        else:
            print("Tienes que logearte nuevamente")#Mensaje de salida del banco
print("Bienvenido al sistema bancario")#Mensaje de bienvenida
saldo_ini = 2000#Saldo inicial
print("Que quieres hacer?")#Pregunta
#Opciones que ofrece el banco  
print("1. Depositar")#opcion 1
print("2. Retirar")#opcion 2
print("3, Ver tu saldo")#opcion 3
print("4. Transferir")#opcion 4
print("5. Salir")#opcion 5
option = input()#Ingreso de opcion
if option == "1":
    print("Cuanto dinero quieres depositar?")
    deposito = int((input()))
    saldo_ini += deposito
    print("Tu saldo es:",saldo_ini)
if option == "2":
    print("Cuanto dinero quieres retirar?")
    retiro = int((input()))
    saldo_ini -= retiro 
    print("Tu saldo es:",saldo_ini)
if option == "3":
    print("Tu saldo es:",saldo_ini)
if option == "4":
    print("Cuanto dinero quieres tranferir:")
    tranferir = int((input()))
    print("El numero de cuenta a transferir debe tener 6 digitos")
    #Que pasa si la cuenta tiene mas de 6 digitos 
    input("Ingresa el numero de cuenta a transferir:")
    saldo_ini -= tranferir
    print("Tu nuevo saldo es:",saldo_ini)
if option == "5":
    print("Gracias por usar nuestro banco")

