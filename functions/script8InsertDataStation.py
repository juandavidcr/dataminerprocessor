import os
import mysql.connector
import re
from datetime import datetime

token = "--------------------------------------"
listaFechaTransformada=[]
listaDeFechas = []
listaPrecipitaciones=[]
listaEvaporacion=[]
listTmax=[]
listTmin=[]


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
    
def getInfoestaciones():
    #,latitud,longitud,altitud_msnm 
    sqlQuery2=f"SELECT id_estacion,num_estacion,nombre_estacion FROM Estacion_climatologica"
    cursor.execute(sqlQuery2)
    result=cursor.fetchall()
    #print(result)
    for filaEstaciones in result:
        # latitud | longitud | altitud_msnm |
        print("| IdEstacion | Estacion Número | Nombre |")
        print(filaEstaciones)



ubicaciondeData="./dataEstaciones/"


archivos = os.listdir(ubicaciondeData)

# Filtrar los archivos con extensión .txt
archivos_txt = [archivo for archivo in archivos if archivo.endswith(".txt")]
# Mostrar los nombres de los archivos txt


getInfoestaciones()
estacion_nombre=input("Ingresar un nombre de estacion valido: ")
getEstacionId(estacion_nombre)

print("------> \nArchivos Disponibles: \n")
ejemplo_nombre_archivo = "./atzalandata.txt"
print("----------> Ejemplo: ",ejemplo_nombre_archivo)
for archivo_txt in archivos_txt:
    print(archivo_txt)
nombre_archivo = input("Ingrese el nombre del archivo como en el ejemplo indicado arriba (con extension .txt): ")

getInfoestaciones()
# Poder dar al usuario la opcion de ver los id de Estacion
print("| IdEstacion | Estacion Número | Nombre |")
idEstacion=input("Ingresa el Id de estacion: ")
# # Leer el contenido del archivo
#^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$
patternDeFechas = r'\b\d{2}/\d{2}/\d{4}\b'
patternDePrecip = r'(\w*)|([0-9]*\.?[0-9]*)'
patternDeEvap = r'(\w*)|([0-9]*\.?[0-9]*)'
patternTmaxyTmin= r'(\w*)|([0-9]*\.?[0-9]*)'

with open(ubicaciondeData+nombre_archivo, 'r') as archivo:
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
print("(Opciones) 1: Si")
print("(Opciones) 2: No")
opcionUsuario=input(f"---------> ¿Deseas insertar datos a la tabla Datos Climatologicos con la estacion con id ----> {idEstacion} <---- en este momento?: ----->(Ten cuidado podrias insertar doble tus datos. Verifica por favor el id de estacion Ingresado)(Escribe 1 o 2): ")
if(opcionUsuario=="1"):
    midb.commit()
archivo.close()       
print("Se creo el archivo Data.sql. Favor de Revisarlo si deseas ingresar de manera manual ese sql.")

with open("./functions/script8.1ReemplazaryAjustar.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)