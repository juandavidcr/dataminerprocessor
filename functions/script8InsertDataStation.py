import mysql.connector
import re
from datetime import datetime

def transform_FechaFormat(fecha_str):
    #print("transformando fecha")
    fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
    fecha_transformada = fecha_obj.strftime("%Y-%m-%d")
    return fecha_transformada

#nombre_archivo = "./bancdata/atzalan/atzalan.txt"
midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
cursor=midb.cursor()

def getEstacionId(estacion_nombre):
    
    #print("Entro a estacionId")
    sqlQuery=f"SELECT id_estacion,num_estacion,nombre_estacion FROM Estacion_climatologica WHERE nombre_estacion LIKE '%{estacion_nombre}%'"
    cursor.execute(sqlQuery)
    result=cursor.fetchall()
    #print(result)
    for fila in result:
        print(fila)
    

ejemplo_nombre_archivo = "./atzalandata.txt"
print("Ejemplo: ",ejemplo_nombre_archivo)
estacion_nombre=input("Ingresar un nombre de estacion valido: ")
nombre_archivo = input("Ingrese el nombre del archivo como en el ejemplo indicado arriba (con extension .txt): ")

# Poder dar al usuario la opcion de ver los id de Estacion
getEstacionId(estacion_nombre)
idEstacion=input("Ingresa el Id de estacion: ")
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
                    #strListResult=str(listResult[0])
                    #trabajar con listatransformada
                    transformada=str(listResult[0])
                    listaFechaTransformada.append(transform_FechaFormat(transformada))
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
#idEstacion=getEstacionId(nombre_archivo)
idEstacionint= int(idEstacion)
y=0
datos_a_insertar=[]
for y in range(nDatos):
    datos_a_insertar.append((listaFechaTransformada[y],float(listaPrecipitaciones[y]),float(listaEvaporacion[y]),float(listTmax[y]),float(listTmin[y]),idEstacionint))

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
#Aqui se inserta a la BD
midb.commit()
archivo.close()       
print("Se creo el archivo Data.sql")