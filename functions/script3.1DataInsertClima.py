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
patternDeFechas = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
token="--------------------------------------"

archivo = open("./atzalandata.txt","r")
for linea in archivo:
    linea=linea.rstrip()
    lPalabras=re.split(r'\s+', linea)
    print(lPalabras)
    # if(lPalabras[0]==token):
    #     break
    # elif (lPalabras[0]==patternDeFechas):
    #     listaFechas.append(lPalabras[0])
    #     for fecha in listaFechas:
    #         print(fecha)
consultaInsertDatosClimat="INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,estacion_id) VALUES(%s,%s,%s,%s,%s,%s)"