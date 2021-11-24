# Proyecto Final
import sys
#Sys es una libreria que se utilizara para finalizar el programa en momentos concretos.
ciclo1=0; azulejoslis=[]; banolis=[]; materialeslis=[]; muebleslis=[]; pisoslis=[]; usuarioslis=[]; ciclo2=0; azulejoslis1=[]; banolis1=[]; materialeslis1=[]; muebleslis1=[]; pisoslis1=[]; usuarioslis1=[]; ciclo3=0; conta=0; men2=0; error=0; error2=0; men3=0; men4=0; error3=0; compra=[]; prod=[]; tiempo=[1]; total=0; usuarioslis2=[]; string="\n"
#Se incializan los contadores y las listas.
print("\n##############")
print("  Construmax   ")
print("##############")
print("\nBienvenido valioso cliente a nuestro servicio de compra virtual.")
#Esta es una breve bienvenida.
while ciclo1!=1 and error!=1:
#Este ciclo permite el uso repetido de el primer menu.
    print("\n1) Sobre nosotros")
    print("\n2) Servicio de compra")
    men1=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
    if men1!=1 and men1!=2:
        print("\nSu respuesta debe corresponder a alguna de las opciones.")
        error=0
        #Este paso valida la entrada de datos para el menu.
    elif men1==1:
        print("\nEn Construmax, nuestro sueno es proveerle materiales y productos de alta calidad a clientes en necesidad de construir un nuevo hogar, porque su felicidad es nuestra felicidad.")
    #Para la primera opcion del primer menu, se establece informacion general de Construmax.
    elif men1==2:
        ciclo2=0
        with open("C:\\Proyectos\\Proyecto Final\\Azulejos, Precios, y Tiempo de Espera.txt","r")as azulejos:
            for i in azulejos.readlines():
                azulejoslis.append(i)
        #Por medio de estas funciones, se obtienen los datos de las bases de datos.
            for i in azulejoslis:
                rep1=i.replace("\n","")
                azulejoslis1.append(rep1)
        #Esta funcion corrige los datos recuperados, removiendo el texto "\n".
        with open("C:\\Proyectos\\Proyecto Final\\Bano, Precios, y Tiempo de Espera.txt","r")as bano:
            for i in bano.readlines():
                banolis.append(i)
            for i in banolis:
                rep2=i.replace("\n","")
                banolis1.append(rep2)
        with open("C:\\Proyectos\\Proyecto Final\\Materiales de Construccion, Precios, y Tiempo de Espera.txt","r")as materiales:
            for i in materiales.readlines():
                materialeslis.append(i)
            for i in materialeslis:
                rep3=i.replace("\n","")
                materialeslis1.append(rep3)
        with open("C:\\Proyectos\\Proyecto Final\\Muebles, Precios, y Tiempo de Espera.txt","r")as muebles:
            for i in muebles.readlines():
                muebleslis.append(i)
            for i in muebleslis:
                rep4=i.replace("\n","")
                muebleslis1.append(rep4)
        with open("C:\\Proyectos\\Proyecto Final\\Pisos, Precios, y Tiempo de Espera.txt","r")as pisos:
            for i in pisos.readlines():
                pisoslis.append(i)
            for i in pisoslis:
                rep5=i.replace("\n","")
                pisoslis1.append(rep5)
        with open("C:\\Proyectos\\Proyecto Final\\Usuarios, Contrasenas, y Presupuestos.txt","r")as usuarios:
            for i in usuarios.readlines():
                usuarioslis.append(i)
            for i in usuarioslis:
                rep6=i.replace("\n","")
                usuarioslis1.append(rep6)
        print("\n##############")
        print("  Bienvenido   ")
        print("##############")
        while ciclo2!=1:
        #Este ciclo permite volver a introducir el usuario en caso de error.
            usu=str(input("Para acceder a nuestro servicio de compra virtual, por favor introduzca su usuario. "))
            if usu in usuarioslis1[1:-1:3]:
            #Aqui se verifica si el usuario se encuentra en la base de datos.
                val=True
            else: 
                val=False
            if val==True:
                ciclo2=1
                ciclo3=0; conta=0
                while ciclo3!=1 and conta!=3:
                #Este ciclo permite volver a introducir la contrasena.
                    contra=str(input("Bienvenido "+str(usu)+", por favor introduzca su contrasena para acceder al programa. "))
                    iusu=usuarioslis1.index(usu)
                    icontra=iusu+1
                    if contra==usuarioslis1[icontra]:
                        val1=True
                    else:
                        val1=False
                    #Por medio de estas funciones se establece si la contrasena introducida pertenece al usuario correspondiente en la base de datos.
                    if val1==True:
                        ciclo3=1
                        print("\n##############################")
                        print("  Servicio de Compra Virtual   ")
                        print("##############################")
                        presunue=float(input("Bienvenido una vez mas "+str(usu)+", por favor introduzca su presupuesto antes de iniciar su compra. "))
                        ipresu=iusu+2
                        usuarioslis1[ipresu]=presunue
                        #Estas funciones reemplazan el valor del presupuesto registrado en la base de datos para el usuario especifico.
                        men2=0; men4=0
                        while men2!=7 and men4!=2:
                        #Este ciclo permite al usuario salirse de menus secundarios.
                            while presunue>0 and men2!=7:
                                men3=0
                                men4=0
                                error2=0
                                print("\n### Menu de Compra Virtual ###")
                                print("1) Azulejos")
                                print("2) Banos")
                                print("3) Materiales de Construccion")
                                print("4) Muebles")
                                print("5) Pisos")
                                print("6) Remover Producto")
                                print("7) Salir")
                                #Se establece el primer menu de productos.
                                while error2!=1:
                                    men3=0
                                    men2=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                    while men3!=6 and men4!=2:
                                        if men2!=1 and men2!=2 and men2!=3 and men2!=4 and men2!=5 and men2!=6 and men2!=7:
                                            print("\nSu respuesta debe corresponder a alguna de las opciones.")
                                            error2=0
                                            men3=6
                                        #Esta funcion valida la respuesta de entrada.
                                        elif men2==1:
                                            error2=1
                                            print("\n### Azulejos ###")
                                            print("1) Azul")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",azulejoslis1[2:4])
                                            print("2) Celeste")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",azulejoslis1[5:7])
                                            print("3) Negro")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",azulejoslis1[8:10])
                                            print("4) Blanco")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",azulejoslis1[11:13])
                                            print("5) Beige")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",azulejoslis1[14:16])
                                            print("6) Salir")
                                            #Se establece el segundo menu de productos.
                                            men3=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                            if men3==1:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*5.99
                                                compra.append(compratotal)
                                                prod.append("Azul: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(3)
                                                #Se agregan los detalles de la compra a una lista. Adicionalmente, se agrega el tiempo de espera a la misma.
                                            elif men3==2:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*8.99
                                                compra.append(compratotal)
                                                prod.append("Celeste: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                            elif men3==3:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*13.99
                                                compra.append(compratotal)
                                                prod.append("Negro: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                            elif men3==4:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*16.99
                                                compra.append(compratotal)
                                                prod.append("Blanco: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(5)
                                            elif men3==5:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*14.99
                                                compra.append(compratotal)
                                                prod.append("Beige: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(3)
                                        elif men2==2:
                                            error2=1
                                            print("\n### Bano ###")
                                            print("1) Retrete")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",banolis1[2:4])
                                            print("2) Regadera")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",banolis1[5:7])
                                            print("3) Lavabo")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",banolis1[8:10])
                                            print("4) Basurero")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",banolis1[11:13])
                                            print("5) Cortina")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",banolis1[14:16])
                                            print("6) Salir")
                                            men3=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                            if men3==1:
                                                compra.append(599.99)
                                                prod.append("Retrete: 599.99")
                                                presunue=presunue-599.99
                                                tiempo.append(5)
                                            elif men3==2:
                                                compra.append(999.99)
                                                prod.append("Regadera: 999.99")
                                                presunue=presunue-999.99
                                                tiempo.append(16)
                                            elif men3==3:
                                                compra.append(499.99)
                                                prod.append("Lavabo: 499.99")
                                                presunue=presunue-499.99
                                                tiempo.append(10)
                                            elif men3==4:
                                                compra.append(89.99)
                                                prod.append("Basurero: 89.99")
                                                presunue=presunue-89.99
                                                tiempo.append(4)
                                            elif men3==5:
                                                compra.append(49.99)
                                                prod.append("Cortina: 49.99")
                                                presunue=presunue-49.99
                                                tiempo.append(3)
                                        elif men2==3:
                                            error2=1
                                            print("\n### Materiales de Construccion ###")
                                            print("1) Granito")
                                            print("Precio (Pesos, por metros cubico), y Tiempo de Espera (Dias):",materialeslis1[2:4])
                                            print("2) Marmol")
                                            print("Precio (Pesos, por metros cubico), y Tiempo de Espera (Dias):",materialeslis1[5:7])
                                            print("3) Cemento")
                                            print("Precio (Pesos, por metros cubico), y Tiempo de Espera (Dias):",materialeslis1[8:10])
                                            print("4) Ladrillo")
                                            print("Precio (Pesos, por metros cubico), y Tiempo de Espera (Dias):",materialeslis1[11:13])
                                            print("5) Vidrio")
                                            print("Precio (Pesos, por metros cubico), y Tiempo de Espera (Dias):",materialeslis1[14:16])
                                            print("6) Salir")
                                            men3=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                            if men3==1:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cubicos que desea comprar. "))
                                                compratotal=cantidad*14.99
                                                compra.append(compratotal)
                                                prod.append("Granito: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(5)
                                            elif men3==2:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cubicos que desea comprar. "))
                                                compratotal=cantidad*19.99
                                                compra.append(compratotal)
                                                prod.append("Marmol: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(7)
                                            elif men3==3:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cubicos que desea comprar. "))
                                                compratotal=cantidad*11.99
                                                compra.append(compratotal)
                                                prod.append("Cemento: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                            elif men3==4:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cubicos que desea comprar. "))
                                                compratotal=cantidad*9.99
                                                compra.append(compratotal)
                                                prod.append("Ladrillo: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(2)
                                            elif men3==5:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cubicos que desea comprar. "))
                                                compratotal=cantidad*18.99
                                                compra.append(compratotal)
                                                prod.append("Vidrio: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                        elif men2==4:
                                            error2=1
                                            print("\n### Muebles ###")
                                            print("1) Sillon")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",muebleslis1[2:4])
                                            print("2) Mesa")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",muebleslis1[5:7])
                                            print("3) Libreria")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",muebleslis1[8:10])
                                            print("4) Escritorio")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",muebleslis1[11:13])
                                            print("5) Cama")
                                            print("Precio (Pesos), y Tiempo de Espera (Dias):",muebleslis1[14:16])
                                            print("6) Salir")
                                            men3=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                            if men3==1:
                                                compra.append(449.99)
                                                prod.append("Sillon: 449.99")
                                                presunue=presunue-449.99
                                                tiempo.append(7)
                                            elif men3==2:
                                                compra.append(299.99)
                                                prod.append("Mesa: 299.99")
                                                presunue=presunue-299.99
                                                tiempo.append(4)
                                            elif men3==3:
                                                compra.append(999.99)
                                                prod.append("Libreria: 999.99")
                                                presunue=presunue-999.99
                                                tiempo.append(10)
                                            elif men3==4:
                                                compra.append(499.99)
                                                prod.append("Escritorio: 499.99")
                                                presunue=presunue-499.99
                                                tiempo.append(8)
                                            elif men3==5:
                                                compra.append(849.99)
                                                prod.append("Cama: 849.99")
                                                presunue=presunue-849.99
                                                tiempo.append(9)
                                        elif men2==5:
                                            error2=1
                                            print("\n### Pisos ###")
                                            print("1) Madera")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",pisoslis1[2:4])
                                            print("2) Marmol")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",pisoslis1[5:7])
                                            print("3) Granito")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",pisoslis1[8:10])
                                            print("4) Piedra")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",pisoslis1[11:13])
                                            print("5) Ceramica")
                                            print("Precio (Pesos, por metros cuadrados), y Tiempo de Espera (Dias):",pisoslis1[14:16])
                                            print("6) Salir")
                                            men3=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                            if men3==1:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*14.99
                                                compra.append(compratotal)
                                                prod.append("Madera: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                            elif men3==2:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*19.99
                                                compra.append(compratotal)
                                                prod.append("Marmol: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(5)
                                            elif men3==3:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*9.99
                                                compra.append(compratotal)
                                                prod.append("Granito: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(3)
                                            elif men3==4:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*7.99
                                                compra.append(compratotal)
                                                prod.append("Piedra: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(4)
                                            elif men3==5:
                                                cantidad=float(input("Por favor introduzca la cantidad de metros cuadrados que desea comprar. "))
                                                compratotal=cantidad*6.99
                                                compra.append(compratotal)
                                                prod.append("Ceramica: "+str(compratotal))
                                                presunue=presunue-compratotal
                                                tiempo.append(3)
                                        elif men2==6:
                                            error2=1
                                            error3=0
                                            print("\n### Remover Producto ###")
                                            print("1) Remover")
                                            print("2) Salir")
                                            while error3!=1:
                                                men4=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                                if men4!=1 and men4!=2:
                                                    print("\nSu respuesta debe corresponder a alguna de las opciones.")
                                                    error3=0
                                                elif men4==1:
                                                    error3=1
                                                    print("\nEsta es su lista hasta ahora.")
                                                    print(prod)
                                                    remover=int(input("Por favor introduzca el numero del producto en la lista que desea remover. "))
                                                    compra.pop(remover-1)
                                                    prod.pop(remover-1)
                                                    #Esta funcion permite remover elementos de la compra.
                                                elif men4==2:
                                                    error3=1
                                        elif men2==7:
                                            error2=1
                                            men3=6
                            if presunue<0:
                                error3=0
                                print("\nHa sobrepasado su presupuesto.")
                                print("\n### Remover Producto ###")
                                print("1) Remover")
                                print("2) Salir")
                                while error3!=1:
                                    men4=int(input("Por favor introduzca el numero de la opcion que desea escoger. "))
                                    if men4!=1 and men4!=2:
                                        print("\nSu respuesta debe corresponder a alguna de las opciones.")
                                        error3=0
                                    elif men4==1:
                                        error3=1
                                        print("\nEsta es su lista hasta ahora.")
                                        print(prod)
                                        remover=int(input("Por favor introduzca el numero del producto en la lista que desea remover. "))
                                        compra.pop(remover-1)
                                        prod.pop(remover-1)
                                    elif men4==2:
                                        error3=1
                        print("\n### Finalizar Compra ###")
                        instalacion=str(input("El precio de instalacion de los productos es $550, ¿Desea comprar este servicio? "))
                        if instalacion=="Si" or instalacion=="SI" or instalacion=="si":
                            for i in compra:
                                total=total+i
                            total=total+550
                            presunue=presunue-550
                            totaliva=total+(total*0.16)
                            #Se agrega al total, el cual se calcula iterando la lista de productos comprados, el precio de la instalacion, y el IVA.
                            print("\nEl total de su compra, mas IVA, es $"+str(totaliva)+".")
                        else:
                            for i in compra:
                                total=total+i
                            totaliva=total+(total*0.16)
                            print("\nEl total de su compra, mas IVA, es $"+str(totaliva)+".")
                        print("\nSu presupuesto restante es $"+str(presunue)+".")
                        usuarioslis1[ipresu]=[presunue]
                        #Se reestablece el presupuesto en la lista para subirlo a la base de datos.
                        print("\nSu pedido llegara en",max(tiempo),"dias.")
                        #Se establece el tiempo de espera del pedido en base al valor mas alto de tiempo de espera, por producto.
                        usuarioslis2=[string+str(i) for i in usuarioslis1[1::]]
                        usuarioslis2.insert(0,"Usuarios, Contrasenas, y Presupuestos:")
                        with open("C:\\Proyectos\\Proyecto Final\\Usuarios, Contrasenas, y Presupuestos.txt","w")as us:
                            for i in usuarioslis2:
                                us.writelines(str(i))
                        #Se reescribe la base de datos con el nuevo presupuesto.
                        res=str(input("¿Desea volver a realizar una compra? "))
                        if res=="si" or res=="Si" or res=="SI":
                            ciclo1=0
                        else:
                            sys.exit()
                    else:
                        print("\nHa introducido la contrasena incorrecta. Por favor intente de nuevo. AVISO, si no logra introducir la contrasena correcta en 3 intentos, el programa se cerrara.")
                        conta=conta+1
                if conta==3:
                    print("\nHa excedido el limite de intentos de acceso. El programa se cerrara.")
                    sys.exit()
                    #Al exceder el numero de intentos (3) para introducir la contrasena correcta, el programa se cierra.
            else:
                print("\nHa introducido un usuario no existente. Por favor intente de nuevo.")