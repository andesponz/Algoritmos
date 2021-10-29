# Usuario y contraseÃ±a
usuario=str(input("Introduzca su usuario. "))
contraseña=int(input("Introduzca su contraseña. "))
error=0
while error!=1:
    if usuario!="ADMIN" or contraseña!=123456:
        print("El usuario y/o la contraseÃ±a son equivocados. ")
        usuario=str(input("Introduzca su usuario. "))
        contraseña=int(input("Introduzca su contraseña. "))
        error=2
        print("\nACCESO DENEGADO")
    else:
        print("\nACCESO PERMITIDO")
        error=1