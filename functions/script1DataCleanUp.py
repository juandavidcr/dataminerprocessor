#!/usr/bin/env python
# decoding: utf-8
#
# 
# Script que separa la información de los txt

import os
import re
import itertools

from pexpect import EOF

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
def getInfoData(route,filename):
    #print(route)
    if os.path.exists(filename):
        os.remove(filename)

    tam=len(listNamesEstacion)
    x =range(tam)
    filename+=".txt"
    if os.path.exists(route):
        with open(route, "r") as text_file:
            #nombre de la estación climatologica a cargar
            #print(listNamesEstacion[i])
            ubicacion="./target/"
            archivoEstacion = open(ubicacion+filename,"a")
            #archivoEstacion = open(listNamesEstacion[i],"a")
            for line in itertools.islice(text_file, 17,countlines(route)):
                archivoEstacion.writelines(line)
                #archivoEstacion.close()
            archivoEstacion.close()
        text_file.close()
    else:
        print('El archivo no existe')    
    return filename

def getInfoDataTable(route,filename2):
    if os.path.exists(filename2):
        os.remove(filename2)
    #print(route)
    
    filename2 += ".txt"
    if os.path.exists(route):
        with open(route, "r") as text_file:
            ubicacion="./target/"
            #se obtienen las cabeceras de los datos de todas las estaciones dentro del sistema de archivos por cada ruta existente
            archivo = open(ubicacion+filename2,"a")
            #de la linea 4 del archivo se identifica un patron de información de las estaciones que ayudara a crear las tablas de municipio, organismo, Estado de la Republica Mexicana y Estación Climatológica.
            for line in itertools.islice(text_file, 4, 17):
                texto=line
                archivo.writelines(texto)
            archivo.close()
            text_file.close()
    else:
        print('El archivo no existe')
    return filename2

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
     


