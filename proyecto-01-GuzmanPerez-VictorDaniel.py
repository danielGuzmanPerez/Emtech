from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


def login():
    # usuario: user
    # contrasenia: user
    intentos = 0
    correcto = False
    while (not correcto):
        if intentos == 3:
            print("Intentos superados, ¡adios!")
            quit()
        usuario = input("\n Ingrese usuario: ")
        password = input("Ingrese Password: ")
        if usuario == "user" and password == "user":
            print("___________________________________________________________________-")
            print("\t \t \t \t \t \t Bienvenido")
            print("___________________________________________________________________-")
            correcto = True
        else:
            print("\n")
            if usuario != "user":
                print("¡Usuario incorrecto!")
            if password != "user":
                print ("Contraseña Incorrecta")
            intentos +=1

def parte1():
    cantidad_ventas= []             # (nombre_producto, numero de ventas, categoria)
    productosMasVendidos=[]         # contiene los cinco productos con mas ventas
    cantidad_busquedas = []         #( nombre_producto, numero de busquedas, categoria)
    productosMasBuscados=[]         #contiene los diez productos mas buscados
    categorias=[]                   #contiene las distintas categorias de los productos
    ventasCategoria=[]              #contiene los productos de cada categoria
    busquedasCategoria=[]           #Contiene los productos de cada categoria
    count = 0
    print("_________________________________________________")
    print("\n\n \t \t Opción 1 Productos más vendidos y productos rezagados")
    print("_________________________________________________")

    #Creando la lista de cantidad ventas (nombre_producto, numero de ventas, categoria)
    #Se recorre primero la lista de productos para comparar cada producto con todas las ventas que hay
    for producto in lifestore_products:
        count=0
        for ventas in lifestore_sales:
            #Se cuenta la cantidad de veces que el id de un producto aparece en la lista de ventas
            if producto[0] == ventas[1] :
                count +=1
        #Se agrega el valor a la lista nueva
        cantidad_ventas.append([producto[1],count,producto[3]])
    # Se ordenan los elementos de menor a mayor basandonos en el numero de ventas posicion 1
    cantidad_ventas = sorted(cantidad_ventas, key= lambda x: x[1] )
    # se guarda en una lista nueva los ultimos cinco elementos de la lista cantidad_ventas, los cuales son los productos mas vendidos
    productosMasVendidos= cantidad_ventas[len(cantidad_ventas)-5 : len(cantidad_ventas)]

    # Creando la lista de cantidad_busquedas (nombre_producto, numero de busquedas, categoria)
    #Busquedas de productos
    for producto in lifestore_products:
        count = 0
        for busquedas in lifestore_searches:
            if producto[0] == busquedas[1]:
                count +=1
        cantidad_busquedas.append([producto[1],count, producto[3]])
    # Se ordenan los elementos de menor a mayor basandonos en el numero de busquedas posicion 1
    cantidad_busquedas = sorted(cantidad_busquedas, key=lambda x: x[1])
    # se guarda en una lista nueva los ultimos diez elementos de la lista cantidad_busquedas, los cuales son los productos mas buscados
    productosMasBuscados = cantidad_busquedas[len(cantidad_busquedas) - 10: len(cantidad_busquedas)]
    productosMasVendidos.reverse()
    productosMasBuscados.reverse()
    print("\n ----------Cinco Productos con mayores ventas----------\n")
    for x in range(0,5):
        print(f"[{x+1}] Nombre: {productosMasVendidos[x][0][:45]}")
        print(f"Numero de ventas: {productosMasVendidos[x][1]}\n")


    print("\n ----------Diez Productos con mayores Busquedas----------\n")
    for x in range(0, 10):
        print(f"[{x+1}] Nombre: {productosMasBuscados[x][0][:45]}")
        print(f"Numero de busquedas: {productosMasBuscados[x][1]}\n")

    #obteniendo las distintas categorias
    for categoria in lifestore_products:
        if categoria[3] not in categorias:
            categorias.append(categoria[3])

    #Obteniendo los productos menos vendidos por categoria
    #por cada categoria se recorre la lista cantidad ventas, si coincide la categoria se almacena en
    #una lista distinta
    print("\n\t\tPor categoria:\n\n")

    for cat in categorias:
        #limpiar la lista temporal
        ventasCategoria =[]
        print(f" ---------------- Categoria: {cat}--------------------")
        for producto in cantidad_ventas:
            #Si las categorias coinciden se almacena en la lista temporal
            if producto[2] == cat:
                ventasCategoria.append(producto)
        #Acomodando la lista de menor a mayor ventas
        ventasCategoria = sorted(ventasCategoria, key=lambda x: x[1])
        #imprimir los productos
        print("\n--------- 5 productos con menores ventas---------\n ")
        for x in range(0,len(ventasCategoria)):
            if x == 5:
                break
            else:
                print(f"[{x + 1}] producto: {ventasCategoria[x][0][:45]}")
                print(f"cantidad de ventas: {ventasCategoria[x][1]}")


        # Obteniendo los productos con menos busquedas
        # por cada categoria se recorre la lista cantidad_busquedas, si coincide la categoria se almacena en
        # una lista distinta

        print("\n----------  10 productos con menores busquedas ---------\n ")
       ## for cat in categorias:
        # limpiar la lista temporal
        busquedasCategoria = []
        #print(f"\nCategoria: {cat}\n ")
        for producto in cantidad_busquedas:
             # Si las categorias coinciden se almacena en la lista temporal
            if producto[2] == cat:
                busquedasCategoria.append(producto)
        # Acomodando la lista de menor a mayor busquedas
        busquedasCategoria = sorted(busquedasCategoria, key=lambda x: x[1])
        # imprimir los productos
        for x in range(0, len(busquedasCategoria)):
            if x == 10:
                break
            else:
                print(f"[{x + 1}] producto: {busquedasCategoria[x][0][:45]}")
                print(f"cantidad de ventas: {busquedasCategoria[x][1]}")
    print("____________________________________________________________")



    




def parte2():
    resenias = [] # (nombre prodcuto, promedio de reseñas) solo si existen reseñas
    productosMejoresResenias = [] #Guarda los cinco productos con mejores reseñas
    productosPeoresResenias = [] #guarda los cinco productos con peores reseñas

    sumaScore=0                 #suma las reseñas de cada prodcuto
    count=0                     #cantidad de reseñas que tiene cada producto
    promedio=0                  #Se promedian las reseñas por producto

    #Se recorre cada uno de los productos existentes
    for producto in lifestore_products:
        sumaScore=0
        count=0
        #Si existe el id de produto en la lista de ventas se suma su score
        for ventas in lifestore_sales:
            if producto[0] == ventas[1]:
                sumaScore+=ventas[2]
                count+=1
        #Se promedia el score de cada producto y se almacena en la lista resenia siempre y cuando existan reseñas
        if count > 0:
            promedio = float(sumaScore / count)
            resenias.append([producto[1],promedio])

     # Se ordenan los elementos de menor a mayor basandonos en el promedio de las reseñas
    resenias = sorted(resenias, key=lambda x: x[1])
    # se guarda en una lista nueva los ultimos diez elementos de la lista cantidad_busquedas, los cuales son los productos mas buscados
    productosMejoresResenias = resenias[len(resenias) - 5: len(resenias)]
    # se guarda en una lista nueva los ultimos diez elementos de la lista cantidad_busquedas, los cuales son los productos mas buscados
    productosPeoresResenias = resenias[0: 5]
    print("_____________________________________________________________-")
    print("\t\t\t Top productos ")
    print("_____________________________________________________________-")
    print("5 Productos con mejores reseñas: ")
    for x in range(0,len(productosMejoresResenias)):
        print(f"\nProducto{x+1}: {productosMejoresResenias[x][0]}")
        print(f" Promedio de reseñas: {productosMejoresResenias[x][1]}")

    print("\n\n5 Productos con peores reseñas: ")
    for x in range(0, len(productosPeoresResenias)):
        print(f"\nProducto{x + 1}: {productosPeoresResenias[x][0]}")
        print(f" Promedio de reseñas: {productosPeoresResenias[x][1]}")

    print("____________________________________________________________")






def parte3():
    meses =["01","02","03","04","05","06","07","08","09","10","11","12"]
    years=[]                # almacena los distintos años encontrados en las fechas de las ventas
    ventasProductos =[]      # (precio producto vendido, fecha, refund)
    ingresoMensual=0        #Total de los ingresos mensuales
    promedioMensual=0       #promedio de las vents de cada mes
    countVentasMensuales = 0     #la cantidad de ventas que se hicieron por mes para lograr sacar el promedio
    totalAnual=0
    ventaMes=[]             #Guardara la venta total de cada mes y se alamcenará en mesesConMasVentas[]
    #Se obtienen los valores para la lista ventasProductos
    for producto in lifestore_products:
        for ventas in lifestore_sales:
            if producto[0] == ventas[1]:
                ventasProductos.append([producto[2],ventas[3],ventas[4]])

    #Se obtienen los distintos años de las fechas
    for ventas in ventasProductos:
        #Year es una variable temporal
        # se divide la fecha de cada venta y se almacenan en 'year' year = [dia,mes,año]
        year = str(ventas[1]).split('/')
        #si la fecha que se está comparando no se encuentre dentro de la lista years se agrega
        if year[2] not in years:
            years.append(year[2])
    years.sort()
    print("___________________________________________________________________-")
    print("\t\t\t Ventas")
    print("___________________________________________________________________-")
        #comparo el mes de cada venta con cada mes de cada distinto año para obtener las ventas mensuales
    for anio in years:
        totalAnual=0
        ventaMes = []
        print("\n\t Año: ",anio)
        for mes in meses:
            ingresoMensual=0
            countVentasMensuales=0
            print("\n\t mes: ", mes)
            for venta in ventasProductos:
                temp = str(venta[1]).split('/')
                #Si el año y mes coinciden con los que se estan comparando actualmente
                # y además no tiene devolución se suma el costo del objeto
                if temp[1] == mes and temp[2] == anio and venta[2] != 1:
                    ingresoMensual +=  venta[0]
                    countVentasMensuales+=1
                    #Si el mes tuvo ventas se saca el promedio de ventas mensuales
            if(countVentasMensuales >0):
                promedioMensual = float(ingresoMensual / countVentasMensuales)
            totalAnual +=ingresoMensual
            print("Ingreso Mensual: $",ingresoMensual)
            print("Cantidad de ventas",countVentasMensuales)
            if(countVentasMensuales >0):
                print("Ventas promedio del mes: $", promedioMensual)
            else:
                print("Ventas promedio del mes: 0")
            ventaMes.append([mes,ingresoMensual])

        #se ordenan los valores de venta mes para que esten de menor a mayor cantidad de ventas
        ventaMes = sorted(ventaMes, key=lambda x: x[1])
        print("\n \t Top tres meses con mejores ventas del año: ")
        print("[1] Mes: ",ventaMes[-1][0], " Ventas: $",ventaMes[-1][1])
        print("[2] Mes: ",ventaMes[-2][0], " Ventas: $",ventaMes[-2][1])
        print("[3] Mes: ",ventaMes[-3][0], " Ventas: $",ventaMes[-3][1])
        print(f"Total de ventas del año {anio}: $",totalAnual)
        print("_________________________________________________")












def menu():
    opcion= 0
    while(opcion !=4):
        print("\n\n MENU ")
        print("[1] Productos más vendidos y productos rezagados")
        print("[2] Productos por reseña en el servicio")
        print("[3] Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año")
        print("[4] Terminar")
        opcion= int(input("\nSelecciona una opcion: "))
        if opcion == 1:
            parte1()
        elif opcion == 2:
            parte2()
        elif opcion == 3:
            parte3()
        elif opcion == 4:
            quit()
        else:
            print("\n opcion incorrecta")




login()
menu()

