#!/usr/bin/env python
# decoding: utf-8
# Script que separa la información de los txt
from functions.script1DataCleanUp import getInfoDataTable,getInfoData

from pexpect import EOF
print("----------------------------------------------------------------------------")
print(f"Bienvenido al programa * UAM springerDataClimateMX *")
print("----------------------------------------------------------------------------")
print(f'Instrucciones: 1.- Cargar archivos de estaciones climatologicas dentro de la carpeta bancdata.\n Por cada carpeta de municipio nombrada poner adentro los archivos de las estaciones pertinentes. Previamente se realizó un análisis de los Organismos que controlan las estaciones climatológicas y se diseño una base de datos para recibir dichos datos con la ayuda de este software.')
# print(f'2.- Correr el script main.py por ejemplo {decorador}--> $ python3 main.py .')
print(f'2.- Crear la base de datos con los catalogos previamente cargados, a continuacion el script de la base de datos\n')

directorio = "./bancdata/"
routeF = directorio+"atzalan/atzalan.txt"
routeF2 = directorio+"briones/briones.txt"
routeF3 = directorio+"chicontepec/chicontepec.txt"
routeF4 = directorio+"coatepec/coatepec.txt"
routeF5 = directorio+"cordoba/cordoba.txt"
routeF6 = directorio+"huatusco/huatusco.txt"
routeF7 = directorio+"los-tuxtlas/san-andres.txt"
routeF8 = directorio+"los-tuxtlas/santiago-tuxtla.txt"
routeF9 = directorio+"los-tuxtlas/sihuapan.txt"
routeF10 = directorio+"los-tuxtlas/tapalapa.txt"
routeF11 = directorio+"misantla/misantla.txt"
routeF12 = directorio+"papantla/papantla.txt"
routeF13 = directorio+"tezonapa/tezonapa-1.txt"
routeF14 = directorio+"tezonapa/tezonapa-2.txt"
routeF15 = directorio+"zongolica/zongolica.txt"

print("3.- Produciremos 2 archivos que contienen ciertos patrones de comportamiento y localización dentro de las fuentes tomadas de un kmz de la aplicacion de google earth del siguiente link: https://smn.conagua.gob.mx/tools/RESOURCES/estacion/EstacionesClimatologicas.kmz  \n El primer archivo nombrado extrae las cabeceras de cada archivo proporcionado en la carpeta del banco de datos y deposita los valores en un nuevo formato de información relevante.\n El segundo archivo contendra los datos de cada estacion ingresados de manera ordenada ")
nombre_archivo = input("Ingrese el nombre del archivo a producir (sin extension *.txt): ")
nombre_datos_archivo= input("Ingrese el nombre del archivo de sus datos para MODELO CONAGUA (sin extension *.txt): ")
#almacenamiento de rutas 
listaData = [routeF,routeF2,routeF3,routeF4,routeF5,routeF6,routeF7,routeF8,routeF9,routeF10,routeF11,routeF12,routeF13,routeF14,routeF15]
n=len(listaData)
listaOpciones=[]
for archivos in listaData:
    archivo1=getInfoDataTable(archivos,nombre_archivo)
    archivo2=getInfoData(archivos,nombre_datos_archivo)
listaOpciones.append(archivo1)
listaOpciones.append(archivo2)
decorador="*"

print(f"Se ingresan: {n} archivos")
print(f"Se generaron los siguientes archivos: {archivo1}, {archivo2}")
print("----------------------------------------------------------------------------")
print(f"\nOpcion 1:Procesar el archivo: {listaOpciones[0]} \nEl cual Inserta datos de Estaciones climatologicas en la base de datos:climatologia_diaria \nOpcion 2: Procesar tus datos correspondiente al archivo {listaOpciones[1]} con el municipio id ingresado por usuario.\n")
opcion = input("Elige una opción (1 o 2): ")
if opcion == "1":
    print(f"Has elegido la opción 1.\n Se leera el archivo {listaOpciones[0]} y finalizará el proceso ")
    # print(type(listaOpciones[0]))
    with open("./functions/script3DataAnalisys.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)

elif opcion == "2":
    print(f"Has elegido la opción 2.\n Se leera el archivo {listaOpciones[1]} y finalizará el proceso ")
    with open("./functions/script8InsertDataStation.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)
    # Aquí puedes colocar el código para el flujo de la opción 2
else:
    print("Opción no válida. Debes elegir entre 1 y 2.")