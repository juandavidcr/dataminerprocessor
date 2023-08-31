import mysql.connector
import re
from helpers.dateFormater import transform_FechaFormat
from models.Estaciones import Estaciones

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
cursor=midb.cursor()

listaFechas = []
listaPrecipitacion=[]
listaEvaporacion=[]
listaTMax=[]
listaTMin=[]
listaEstacionId=[]


# nombre_archivo = "./atzalandata.txt"
nombre_archivo = "./1_datafile.txt"
subcadena = "PRECIP"
subcadena2 = "EVAP"
subcadena3 = "TMAX"
subcadena4 = "TMIN"

# Leer el archivo línea por línea y buscar la subcadena
with open(nombre_archivo, 'r') as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        posicion = linea.find(subcadena)
        if posicion != -1:
            print(f"La subcadena '{subcadena}' encontrada en la línea {numero_linea} en la posición {posicion}.")
            print(f"La subcadena '{subcadena2}' encontrada en la línea {numero_linea} en la posición {posicion}.")
            print(f"La subcadena '{subcadena3}' encontrada en la línea {numero_linea} en la posición {posicion}.")
            print(f"La subcadena '{subcadena4}' encontrada en la línea {numero_linea} en la posición {posicion}.")
