#!/usr/bin/env python
# decoding: utf-8
#
# 
# Script que separa la información de los txt

import os
import re
import itertools

from pexpect import EOF
#armado de rutas
# directorio = "./bancdata/"
# routeF = directorio+"atzalan/atzalan.txt"
# routeF2 = directorio+"briones/briones.txt"
# routeF3 = directorio+"chicontepec-suspendida/chicontepec.txt"
# routeF4 = directorio+"coatepec-suspendida/coatepec.txt"
# routeF5 = directorio+"cordoba-suspendida/cordoba.txt"
# routeF6 = directorio+"huatusco-suspendida/huatusco.txt"
# routeF7 = directorio+"los-tuxtlas/san-andres.txt"
# routeF8 = directorio+"los-tuxtlas/santiago-tuxtla.txt"
# routeF9 = directorio+"los-tuxtlas/sihuapan.txt"
# routeF10 = directorio+"los-tuxtlas/tapalapa.txt"
# routeF11 = directorio+"misantla/misantla.txt"
# routeF12 = directorio+"papantla/papantla.txt"
# routeF13 = directorio+"tezonapa-suspendida/tezonapa-1.txt"
# routeF14 = directorio+"tezonapa-suspendida/tezonapa-2.txt"
# routeF15 = directorio+"zongolica-suspendida/zongolica.txt"

#almacenamiento de rutas 
#listaData = [routeF,routeF2,routeF3,routeF4,routeF5,routeF6,routeF7,routeF8,routeF9,routeF10,routeF11,routeF12,routeF13,routeF14,routeF15]
#creacion de nombres de cada banco de datos
sufixFile = ".txt"
namefile = "data"

listNamesEstacion = [
    "./target/atzalan."+namefile+sufixFile,
    "./target/briones."+namefile+sufixFile,
    "./target/chicontepec."+namefile+sufixFile,
    "./target/coatepec."+namefile+sufixFile,
    "./target/cordoba."+namefile+sufixFile,
    "./target/huatusco."+namefile+sufixFile,
    "./target/san-andres."+namefile+sufixFile,
    "./target/santiago-tuxtla."+namefile+sufixFile,
    "./target/sihuapan."+namefile+sufixFile,
    "./target/tapalapa."+namefile+sufixFile,
    "./target/misantla."+namefile+sufixFile,
    "./target/papantla."+namefile+sufixFile,
    "./target/tezonapa-1."+namefile+sufixFile,
    "./target/tezonapa-2."+namefile+sufixFile,
    "./target/zongolica."+namefile+sufixFile
]

#Funcion encargada de separar las cabeceras de los datos en bruto
def getInfoData(route):
    print(route)
    tam=len(listNamesEstacion)
    x =range(tam)
    
    if os.path.exists(route):
        with open(route, "r") as text_file:
            #nombre de la estación climatologica a cargar
            #print(listNamesEstacion[i])
            archivoEstacion = open("datafile.txt","a")
            #archivoEstacion = open(listNamesEstacion[i],"a")
            for line in itertools.islice(text_file, 17,countlines(route)):
                archivoEstacion.writelines(line)
                #archivoEstacion.close()
            archivoEstacion.close()
        text_file.close()
    else:
        print('El archivo no existe')

def getInfoDataTable(route):
    print(route)
    if os.path.exists(route):
        with open(route, "r") as text_file:
            #se obtienen las cabeceras de los datos de todas las estaciones dentro del sistema de archivos por cada ruta existente
            archivo = open("newfile.txt","a")
            #de la linea 4 del archivo se identifica un patron de información de las estaciones que ayudara a crear las tablas de municipio, organismo, Estado de la Republica Mexicana y Estación Climatológica.
            for line in itertools.islice(text_file, 4, 17):
                texto=line
                archivo.writelines(texto)
            archivo.close()
            text_file.close()
    else:
        print('El archivo no existe')
#captura la informacion de cada archivo divdiendo y poniendo el nombre correspondiente de  cada banco de datos

#funcion auxiliar para conteo de lineas
def countlines(filein):
    fin = open(filein, "r")
    return len(fin.readlines())
#funcion para hacer pruebas de lectura de lineas y escritura de lineas por archivo recibe la ruta del archivo
def printlineas(route):
    print(route)
    if os.path.exists(route):
        datos=[]
        # with open(route, "r") as text_file:
        archivo = open(route)
        file_lines = archivo.readlines()
        for linea in file_lines:
            datos.append(linea.strip('\n'))
            print(linea)
            #gnerar un diccionario por cada llave de dicc nombre del dicc: Identificacion [ESTACION]= 
            datos = linea.split(" : ") 
            #obtner llave y valor en el 
            #identificacion[datos[0]] = datos[1] 
            #de que lienas estoy leyendo el archivo
            #validar :\s
            #
            # 1. Leer línea por línea del archivos:
            # 1.1. Comparar si es línea de identificación:
            # -- Si tiene como subcadena alguna de las líneas de 1 a 19:
            # ---Generar el SQL para insertar en la tabla de identificaciones
            # -- Si es línea de datos, debe tener "/"
            # ---Generar el SQL para insertar en la tabla de datos 
            # por cada archivo txt que tengo correr el script de la base
            # insert primero la estacion id
            # convertir 
            # #
    else:
        print('El archivo no existe')
    print(datos) 
     

# #Genera elarchivo de los encabezados y el archivo de los datos de cada estación por nombre dejandole un sufijo de la siguiente manera 'nombredelarchivo'+'data'+.txt y newfile.txt contendra las cabeceras de las estaciones para saber el numero de estaciones.
# for x in listaData:
#     #getInfoDataTable(x)
#     getInfoData(x)
