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
print(""" 
Esquemas: 
---------------------------------------------
DROP DATABASE IF EXISTS climatologia_diaria;
CREATE DATABASE climatologia_diaria;
USE climatologia_diaria;
CREATE TABLE Organismo(
    id_organismo int(10) NOT NULL AUTO_INCREMENT,
    nombre_org varchar(255),
    PRIMARY KEY (id_organismo)
);
CATALOGO ORGANISMO
INSERT INTO Organismo VALUES (1,'CONAGUA-SMN'),(2,'CONAGUA-DGE');

CREATE TABLE Estados_Republica_Mex(
id_estado int(5) NOT NULL AUTO_INCREMENT,
nombre_estado varchar(255)
);
CATALOGO DE ESTADOS DE LA REPUBLICA MEXICANA
INSERT INTO climatologia_diaria.Estados_Republica_Mex (id_estado,nombre_estado) VALUES
    (1,'Aguascalientes'),
    (2, 'Baja California'),
    (3, 'Baja California Sur'),
    (4, 'Campeche'),
    (5, 'Coahuila de Zaragoza'),
    (6, 'Colima'),
    (7, 'Chiapas'),
    (8, 'Chihuahua'),
    (9, 'Distrito Federal'),
    (10, 'Durango'),
    (11, 'Guanajuato'),
    (12, 'Guerrero'),
    (13, 'Hidalgo'),
    (14, 'Jalisco'),
    (15, 'México'),
    (16, 'Michoacán de Ocampo'),
    (17, 'Morelos'),
    (18, 'Nayarit'),
    (19, 'Nuevo León'),
    (20, 'Oaxaca de Juárez'),
    (21, 'Puebla'),
    (22, 'Querétaro'),
    (23, 'Quintana Roo'),
    (24, 'San Luis Potosí'),
    (25, 'Sinaloa'),
    (26, 'Sonora'),
    (27, 'Tabasco'),
    (28, 'Tamaulipas'),
    (29, 'Tlaxcala'),
    (30, 'Veracruz de Ignacio de la Llave'),
    (31, 'Yucatán'),
    (32, 'Zacatecas');

CREATE TABLE Municipio(
    id_municipio int(10) NOT NULL AUTO_INCREMENT,
    estado_id int(5),
    nombre_mun varchar(255),
    PRIMARY KEY (id_municipio),
    FOREIGN KEY (estado_id) REFERENCES Estados_Republica_Mex(id_estado)
);
INSERT INTO `Municipio` VALUES (1,30,'ATZALAN'),(2,30,'COATEPEC'),(3,30,'CHICONTEPEC'),(4,30,'COATEPEC 2'),(5,30,'CORDOBA'),(6,30,'HUATUSCO'),(7,30,'SAN ANDRES TUXTLA'),(8,30,'SANTIAGO TUXTLA'),(9,30,'SAN ANDRES TUXTLA 2'),(10,30,'SANTIAGO TUXTLA 2'),(11,30,'MISANTLA'),(12,30,'PAPANTLA'),(13,30,'TEZONAPA'),(14,30,'TEZONAPA 2'),(15,30,'ZONGOLICA');
      
DROP TABLE IF EXISTS Estacion_climatologica; 
#SE VA LLENAR DEPENDIENDO DE ID MUNICIPIO Y ID ORGANISMO
CREATE TABLE Estacion_climatologica (
    id_estacion int(20) NOT NULL AUTO_INCREMENT ,
    num_estacion varchar(50),
    nombre_estacion varchar(255),
    situacion varchar(255),
    municipio_id int(10),
    organismo_id int(10),
    latitud varchar(50),
    longitud varchar(50),
    altitud_msnm varchar(50),
    emision_fecha DATE,
    PRIMARY KEY (id_estacion),
    FOREIGN KEY (municipio_id) REFERENCES Municipio(id_municipio),
    FOREIGN KEY (organismo_id) REFERENCES Organismo(id_organismo)
);

CREATE TABLE Datos_Climatologicos(
    # id_climatologicos int(10) NOT NULL AUTO_INCREMENT,
    # fecha DATE,
    # precipitacion_mm FLOAT(5,1),
    # evaporacion_mm FLOAT(5,1),
    # tmax FLOAT(3,1),
    # tmin FLOAT(3,1),
    # humedad_relativa FLOAT(4,2),
    # estacion_id int(20),
    # PRIMARY KEY (id_climatologicos),
    # FOREIGN KEY (estacion_id) REFERENCES Estacion_climatologica(id_estacion)
 );   
 """)

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