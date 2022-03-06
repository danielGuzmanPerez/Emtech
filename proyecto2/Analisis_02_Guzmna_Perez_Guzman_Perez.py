import pandas as pd
import matplotlib.pyplot as plt

sldb = pd.read_csv('synergy_logistics_database.csv', index_col=0, parse_dates=[5])

opcion=0

"""
Analisis para las 10 rutas
"""
def rutas(importacion, exportacion):
    topRutasImportacion(importacion)
    valorImportacion()
    topRutasExportacion(exportacion)
    valorExportacion()

    # Se obtiene el top 10 de importaciones
def topRutasImportacion(importacion):
    # las agrupo por origen, destino y metodo de transporte ya que son las columnas que forman una ruta
    importacion = importacion.groupby(by=['origin', 'destination', 'transport_mode'])

    topImportacion = importacion.count()

    # se acomodan los valores de mayor a menor
    topImportacion = topImportacion.sort_values(by='company_name', ascending=False)

    # se obtienen los 10 primeros
    topImportacion = topImportacion.head(10)['total_value']
    print("\n ------------ Top 10 rutas de importacion mas demandadas-------------")
    print(topImportacion)


    # Se obtiene el top 10 de exportaciones
def valorImportacion():
    rutas = sldb.groupby(['direction', 'origin', 'destination', 'transport_mode'])
    suma = rutas.sum()['total_value']
    rutas = rutas['total_value'].describe()

    rutas['suma_total'] = suma
    rutas = rutas.reset_index()
    # %%
    """
    Analisis para exportaciones: Top 10 rutas por demanda y por ganancias
    """
    importaciones = rutas[rutas['direction'] == 'Imports']
    most_used =  importaciones.sort_values(by='count', ascending=False).head(10)

    valor_total_importaciones =  importaciones['suma_total'].sum()
    valor_total_top = most_used.suma_total.sum()
    total_usos = most_used['count'].sum()
    porcentaje = (valor_total_top / valor_total_importaciones) * 10000
    porcentaje = int(porcentaje) / 100

    print(f'Las 10 rutas mas demandadas de importacion aportan {porcentaje}% de las ganancias, en un total de {total_usos} servicios')


def topRutasExportacion(Exportacion):
    # las agrupo por origen, destino y metodo de transporte ya que son las columnas que forman una ruta
    topExportacion = Exportacion.groupby(by=['origin', 'destination', 'transport_mode']).count()
    # se acomodan los valores de mayor a menor
    topExportacion = topExportacion.sort_values(by='company_name', ascending=False)
    topExportacion = topExportacion.head(10)['total_value']
    print("\n ------------ Top 10 rutas de exportacion mas demandadas-------------")
    print(topExportacion)

def valorExportacion():
    rutas = sldb.groupby(['direction', 'origin', 'destination', 'transport_mode'])
    suma = rutas.sum()['total_value']
    rutas = rutas['total_value'].describe()

    rutas['suma_total'] = suma
    rutas = rutas.reset_index()
    # %%
    """
    Analisis para exportaciones: Top 10 rutas por demanda y por ganancias
    """
    exportaciones = rutas[rutas['direction'] == 'Exports']
    most_used = exportaciones.sort_values(by='count', ascending=False).head(10)

    valor_total_exportaciones = exportaciones['suma_total'].sum()
    valor_total_top = most_used.suma_total.sum()
    total_usos = most_used['count'].sum()
    porcentaje = (valor_total_top / valor_total_exportaciones) * 10000
    porcentaje = int(porcentaje) / 100

    print(f'Las 10 rutas mas demandadas aportan {porcentaje}% de las ganancias, en un total de {total_usos} servicios')

def mediosDeTransporte(importacion, exportacion):
    topMediosTransporteImportacion(importacion)
    topMediosTransporteExportacion(exportacion)

def topMediosTransporteImportacion(importacion):
    #Suma el total_value de cada medio de transporte
    sum= importacion.groupby(by=['transport_mode']).sum()['total_value']
    # las agrupo por medio de transporte
    topImportacion = importacion.groupby(by=['transport_mode']).count()
    # se acomodan los valores de mayor a menor
    topImportacion = topImportacion.sort_values(by='total_value', ascending=False)
    # se obtienen los 10 primeros
    topImportacion = topImportacion.head(3)['total_value']


    print("\n ------------ Top 3 medios de transporte mas utilizados en importacion-------------")
    print(topImportacion)
    print("\n ------------  Medios de transporte que más aportan en importaciones-------------")
    print(sum)

def topMediosTransporteExportacion(Exportacion):
    #Suma el total_value de cada medio de transporte
    sum= Exportacion.groupby(by=['transport_mode']).sum()['total_value']
    # las agrupo por medio de transporte
    topExportacion = Exportacion.groupby(by=['transport_mode']).count()
    # se acomodan los valores de mayor a menor
    topExportacion = topExportacion.sort_values(by='total_value', ascending=False)
    # se obtienen los 10 primeros
    topExportacion= topExportacion.head(3)['total_value']


    print("\n ------------ Top 3 medios de transporte mas utilizados en Exportacion-------------")
    print(topExportacion)
    print("\n ------------  Medios de transporte que más aportan en Exportaciones-------------")
    print(sum)

def valorTotal(importacion, exportacion):
    valorTotalImportación(importacion)
    valorTotalExportación(exportacion)

def valorTotalImportación(importacion):
    #Obteniendo el total de las ventas de todas las importaciones
    DineroTotal= importacion['total_value'].sum()
    print("\n -------------------Importaciones----------------------")
    print(f"\nCantidad total de las importaciones ${DineroTotal}\n")
    #obteniendo los distintos valores de la columna origin
    paises=importacion["origin"].unique()
    total=[]
    porcentaje=[]

    #este for obtiene la suma de ventas de cada pais
    for origen in paises:
        source = importacion.loc[importacion['origin'] == origen]
        total.append( source['total_value'].sum())
        sumaDeValores= sum(total)

    #Obtengo el porcentaje de ventas de cada pais
    for x in range(0,len(total)):
        porcentaje.append([paises[x],(100/sumaDeValores)*total[x],total[x]])

    porcentaje = sorted(porcentaje, key=lambda x: (x[2]))
    porcentaje.reverse()

    #Se imprimen los resultados
    for i in porcentaje:
        print(f"Pais: {i[0]},\tporcentaje: {i[1]}\tcantidad de ventas: {i[2]}")


def valorTotalExportación(exportacion):
    # Obteniendo el total de las ventas de todas las exportaciones
    DineroTotal = exportacion['total_value'].sum()
    print("\n -------------------Exportaciones----------------------")
    print(f"\nCantidad total de las exportaciones ${DineroTotal}\n")
    # obteniendo los distintos valores de la columna origin
    paises = exportacion["origin"].unique()
    total = []
    porcentaje = []

    # este for obtiene la suma de ventas de cada pais
    for origen in paises:
        source = exportacion.loc[exportacion['origin'] == origen]
        total.append(source['total_value'].sum())
        sumaDeValores = sum(total)

    # Obtengo el porcentaje de ventas de cada pais
    for x in range(0, len(total)):
        porcentaje.append([paises[x], (100 / sumaDeValores) * total[x], total[x]])

    porcentaje = sorted(porcentaje, key=lambda x: (x[2]))
    porcentaje.reverse()

    # Se imprimen los resultados
    for i in porcentaje:
        print(f"Pais: {i[0]}\tporcentaje: {i[1]}\tcantidad de ventas: {i[2]}")


def main():
    # Obtengo solo las tuplas que son importacion
    importacion = sldb[sldb['direction'] == "Imports"]

    # Obtengo solo las tuplas que son exportacion
    exportacion = sldb[sldb['direction'] == "Exports"]
    opcion=0

    while opcion != 4:
        print(      "___________________________Opciones______________________________\n[1]. Rutas mas demandadas\n[2]. Medios de transporte utilizados\n[3]. Valor importaciones / exportaciones\n[4]. Terminar")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            rutas(importacion, exportacion)
        elif opcion == '2':
            mediosDeTransporte(importacion, exportacion)
        elif opcion == '3':
            valorTotal(importacion,exportacion)

main()

