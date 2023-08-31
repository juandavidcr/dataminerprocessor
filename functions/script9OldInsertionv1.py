#!/usr/bin/env python
# decoding: utf-8
#
import mysql.connector
import re
from datetime import date
from helpers.dateFormater import transform_FechaFormat

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
cursor=midb.cursor()

def getEstacionId():
    hCddEstacionId=92
    hCddEstacionIdCode=30012
    print("Entro a estacionId")
    sqlQuery=f"SELECT id_estacion FROM Estacion_climatologica WHERE num_estacion='{hCddEstacionIdCode}'"
    cursor.execute(sqlQuery)
    result=cursor.fetchall()
    print(result)
    return hCddEstacionId

patternDeFechas = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
patternDePrecip = '(Nulo*)|[0-9]*\.?[0-9]*'
patternDeEvap = '(Nulo*)|([0-9]*\.?[0-9]*)'
patternTmaxyTmin='(Nulo*)|([0-9]*\.?[0-9]*)'
token = "--------------------------------------"

listResult=[]
listaDeFechas = []
listaPrecipitaciones=[]
listaEvaporacion=[]
listTmax=[]
listTmin=[]
nuevaLista=[]

#archivo = open("./coatepecdata.txt")
archivo = open("./atzalandata.txt")
#archivo = open("./datafile.txt")
for linea in archivo:
    linea = linea.rstrip("\n") 
    listResult=re.split(r'\s+', linea)
    print(listResult)
    n=len(listResult)
    print("Numero de palabras en linea: ",n)
    if n >1:
        if(token==listResult[0]):
            print("saliendo del programa...")
            break
        if(listResult[0]==patternDeFechas or n == 5):
            listaDeFechas.append(listResult[0])
            fechasN=len(listaDeFechas)
            print(listaDeFechas[0])
            print("fechasN: ",fechasN)
    # if n>=1:
        # for numero_linea, linea in enumerate(archivo, start=1):
            # print(f"Línea {numero_linea}: {linea.strip()}")
#     resultFecha = re.match(patternDeFechas, listResult[0])
#     resultPrecipitacion=re.match(patternDePrecip, listResult[1])
#     resultEvaporacion=re.match(patternDeEvap, listResult[2])
#     resultTmax=re.match(patternTmaxyTmin, listResult[3])
#     resultTmin=re.match(patternTmaxyTmin, listResult[4])
#     if resultFecha:
#         #print("Longitud: ---->ListResult[0]",len(listResult[0]))
#         listaDeFechas.append(listResult[0])        
#     if resultPrecipitacion:
#         listaPrecipitaciones.append(listResult[1])        
#     if resultEvaporacion:
#         listaEvaporacion.append(listResult[2])
#     if resultTmax:
#         listTmax.append(listResult[3])
#     if resultTmin:
#         listTmin.append(listResult[3])
# print(listaDeFechas,len(listaDeFechas))
# print(listaPrecipitaciones,len(listaPrecipitaciones))
# print(listaEvaporacion,len(listaEvaporacion))
# print(listTmax,len(listTmax))
# print(listTmin,len(listTmin))
# print(type(listaDeFechas))
# strFecha = str(listaDeFechas[0])
# #print(strFecha)
# #print(type(strFecha))
# nuevaLista =strFecha.split('/')
# #print("nuevaLista",nuevaLista)
# dia=nuevaLista[0]
# mes=nuevaLista[1]
# anyo=nuevaLista[2]
# fechaa = createFecha(anyo,mes,dia)

#INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` (`id_climatologicos`, `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) VALUES ('2', '1999-01-01', '0.0', '', '12.0', '11.0', '', '1');
#primerDatoPrecipMM = str(listaPrecipitaciones[0])
#num_primerDatoPrecipMM = float(listaPrecipitaciones[4])
#primerDatoEvMM=str(listaEvaporacion[0])
#num_primerDatoEvMM = float(listaEvaporacion[4])
#primerDatoTmax=str(listTmax[4])
#num_Tmax=float(primerDatoTmax)
#primerDatoTmin=str(listTmin[4])
#num_Tmin=float(primerDatoTmin)
#hr=None
#estacionID=getEstacionId()
#y=0
#consultaInsertSQLDatoClimatologico=f"INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,estacion_id) VALUES('{transform_FechaFormat(str(listaDeFechas[y]))}',{num_primerDatoPrecipMM},{num_primerDatoEvMM},{num_Tmax},{num_Tmin},{estacionID})"
#print(consultaInsertSQLDatoClimatologico)
# print("""
# INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` ( `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) 
# VALUES ( '"+fechaa+"')
# """)