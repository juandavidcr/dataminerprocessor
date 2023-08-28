import mysql.connector
import re
from helpers.dateFormater import transform_FechaFormat

#nombre_archivo = "./bancdata/atzalan/atzalan.txt"
midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
cursor=midb.cursor()
nombre_archivo = "./atzalandata.txt"
idEstacion=92
token = "--------------------------------------"
listaFechaTransformada=[]
listaDeFechas = []
listaPrecipitaciones=[]
listaEvaporacion=[]
listTmax=[]
listTmin=[]
# # Leer el contenido del archivo
#^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$
patternDeFechas = r'\b\d{2}/\d{2}/\d{4}\b'
patternDePrecip = r'(\w*)|([0-9]*\.?[0-9]*)'
patternDeEvap = r'(\w*)|([0-9]*\.?[0-9]*)'
patternTmaxyTmin= r'(\w*)|([0-9]*\.?[0-9]*)'

with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
        linea = linea.rstrip("\n")
        listResult=re.split(r'\s+', linea)
        for lineasTexto in listResult:
            if(listResult[0]==token):
                break
            if(listResult[0]==''):
                cabecera=lineasTexto
                #print(cabecera.split('\s'))
            if(listResult[0]!=''):
                #print(lineasTexto.split('\s'))
                if(re.search(patternDeFechas,lineasTexto)):
                    listaDeFechas.append(listResult[0])
                    strListResult=str(listResult[0])
                    #trabajar con listatransformada
                    listaFechaTransformada.append(transform_FechaFormat(strListResult))
                if(re.search(patternDePrecip,lineasTexto)):
                    listaPrecipitaciones.append(listResult[1])
                if(re.search(patternDeEvap,lineasTexto)):
                    listaEvaporacion.append(listResult[2])
                if(re.search(patternTmaxyTmin,lineasTexto)):
                    listTmax.append(listResult[3])
                if(re.search(patternTmaxyTmin,lineasTexto)):
                    listTmin.append(listResult[4])    
                   
nDatos=len(listaFechaTransformada)
listaEvaporacion=[0 if elemento == "Nulo" else elemento for elemento in listaEvaporacion]
listaPrecipitaciones = [0 if elemento == "Nulo" else elemento for elemento in listaPrecipitaciones]
listTmax = [0 if elemento == "Nulo" else elemento for elemento in listTmax]
listTmin = [0 if elemento == "Nulo" else elemento for elemento in listTmin]

y=0
datos_a_insertar=[]
for y in range(nDatos):
    datos_a_insertar.append((listaFechaTransformada[y],float(listaPrecipitaciones[y]),float(listaEvaporacion[y]),float(listTmax[y]),float(listTmin[y]),92))

nuevo_archivo = "Data.sql"
with open(nuevo_archivo,'w') as archivoSQL:
    lineaSql= f"INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,estacion_id) VALUES"
    archivoSQL.write(lineaSql)
    for tuplastransformadas in datos_a_insertar:
        lineaSql=str(tuplastransformadas)
        archivoSQL.write(lineaSql+", \n")
        #print(lineaSql)
    archivoSQL.write(";")
    archivoSQL.close()

consultaInsertSQLDatoClimatologico="INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,estacion_id) VALUES(%s,%s,%s,%s,%s,%s)"

cursor.executemany(consultaInsertSQLDatoClimatologico, datos_a_insertar)
#midb.commit()

archivo.close()       
