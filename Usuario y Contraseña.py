# Usuario y contraseña
usuario=str(input("Introduzca su usuario. "))
contrase�a=int(input("Introduzca su contrase�a. "))
error=0
while error!=1:
    if usuario!="ADMIN" or contrase�a!=123456:
        print("El usuario y/o la contraseña son equivocados. ")
        usuario=str(input("Introduzca su usuario. "))
        contrase�a=int(input("Introduzca su contrase�a. "))
        error=2
        print("\nACCESO DENEGADO")
    else:
        print("\nACCESO PERMITIDO")
        error=1