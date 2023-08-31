#!/usr/bin/env python
# decoding: utf-8
#
import mysql.connector
import re
from datetime import datetime

def transform_FechaFormat(fecha_str):
    #print("transformando fecha")
    fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
    fecha_transformada = fecha_obj.strftime("%Y-%m-%d")
    return fecha_transformada

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)

listaMun=[]
listaMunId=[]
listaOrg=[]
listaEstaciones=[]
listaNombreEstaciones=[]
listaSituacion=[]
listaLat=[]
listaLon=[]
listaAlt=[]
listaEmision=[]
listaEmision2=[]
listaIdorgNum=[]


def convertResultOrdIdTostring(resultadoOrgId):
    resultado1= resultadoOrgId[0]
    resultado1=str(resultado1).replace("(","")
    resultado1=resultado1.replace(")","")
    resultado1=resultado1.replace(",","")
    return resultado1

cursor=midb.cursor()

filename = input("Ingrese el nombre del archivo indicado arriba (con extension .txt): ")

archivo = open(filename,"r")

for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    #listResult=re.split(r':', linea)
    #print(listResult)
    if(listResult[0]=='ESTACION'):
        #print("Num Estacion")
        
        listaEstaciones.append(listResult[2])
        

    if(listResult[0]=='NOMBRE'):
        n=len(listResult)
        
        if(n==4):
           listaNombreEstaciones.append(f"{str(listResult[2])} {str(listResult[3])}")
        if (n==5):
            listaNombreEstaciones.append(f"{str(listResult[2])} {str(listResult[3])} {str(listResult[4])}")
        if (n==6):
            listaNombreEstaciones.append(f"{str(listResult[2])} {str(listResult[3])} {str(listResult[4])} {str(listResult[5])}")
        if (n==7):
            listaNombreEstaciones.append(f"{str(listResult[2])} {str(listResult[3])} {str(listResult[4])} {str(listResult[5])} {str(listResult[6])}")
    if(listResult[0] == 'LONGITUD'):
        listaLon.append(str(listResult[2]).replace("�","°"))
        
    if(listResult[0] == 'LATITUD'):
        listaLat.append(str(listResult[2]).replace("�","°"))
       
    if(listResult[0]=='ORGANISMO'):
        #print("---organismo-list---")
        sqlOrgId=f"SELECT id_organismo FROM Organismo WHERE nombre_org like '{listResult[2]}'"
        
        cursor.execute(sqlOrgId)
        resultadoOrgId=cursor.fetchall()
        
        orgIdStr=convertResultOrdIdTostring(resultadoOrgId)
        listaOrg.append(orgIdStr)
        listaIdorgNum.append(int(orgIdStr))
    # Armar query de Estacion Climatologica
    if(listResult[0]=='MUNICIPIO'):
        sqlListMunNombre = "SELECT nombre_mun FROM Municipio;"
        
        cursor.execute(sqlListMunNombre)
        resultadoMunNombre=cursor.fetchall()
        
        numMunicipios = len(resultadoMunNombre)
        for j in range(numMunicipios):
            sqlSelectMunId="SELECT id_municipio FROM Municipio WHERE nombre_mun="+str(resultadoMunNombre[j])+";";
            cleaningx = sqlSelectMunId.replace(",)", "")
            cleaningx2=cleaningx
            cleanedSQL=cleaningx2.replace("(","")
            
            cursor.execute(cleanedSQL)
            
            resultadoMunId=cursor.fetchall()

            numMunId=len(resultadoMunId)
            resultadoMunId=str(resultadoMunId).replace("(","").replace("[","",1).replace("]","",1).replace(",)","",1)

            idMunicipio=resultadoMunId
            
            listaMun.append(listResult[2])
            listaMunId.append(int(idMunicipio))
            cleaningy1 = str(resultadoMunId).replace("[","",1)
            cleanedy2=cleaningy1.replace("(","")
            cleanedMunId=cleanedy2.replace(",)","",1)
            MunicipioIdCleaned=cleanedMunId.replace("]","",1)
            
            #print("cleanedSQL____________->",cleanedSQL)
            #print("Municipio Id: ",resultadoMunId)

    if(listResult[0]=='ALTITUD'):
        listaAlt.append(listResult[2]+' '+listResult[3])
    if(listResult[0]=='EMISION'):
        listaEmision.append(listResult[2])
        fecha_str = listaEmision[0]  
        dateOfDataWeather=transform_FechaFormat(fecha_str)        
        listaEmision2.append(dateOfDataWeather)
    if(listResult[0]=='SITUACI�N'):
        listaSituacion.append(listResult[2])
    
#print(listResult)
#print(listaLat2,listaLon2)
#print(listaIdorgNum,listaMunId)

#print("---------> cleanedMunId: ",MunicipioIdCleaned)
#print(" lMunID: --------->",listaMunId)
# print("resultado ---> Municipio Nombre: ",resultadoMunNombre)
# print("Numero de Estacion: ",listaEstaciones)
# print("NOMBRE ESTACION: ",listaNombreEstaciones)
# print("LISTA ALTITUD: ",listaAlt)
# print("SITUACI�N: ",listaSituacion)
# print("lista EMISION--> ",listaEmision2)
#print("LISTA ORGANIZAION ID------>",listaOrg)
#print("Municipios: lista----------->",listaMun)
#print("OrgIds Lista:------>",listaIdorgNum)

print("------------> numero de municipios: ",numMunicipios)
x=0
datos_a_insertar = []
for x in range(numMunicipios):
    datos_a_insertar.append((listaEstaciones[x],listaNombreEstaciones[x],listaSituacion[x],listaMunId[x],listaIdorgNum[x],listaLat[x],listaLon[x],listaAlt[x],listaEmision2[x])) 

#ESCRIBE EL ARCHIVO DE COMPROBACION
nombre_archivo = "Stations.sql"
with open(nombre_archivo, 'w') as archivoSQL:
    lineaSql = f"INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion,situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES"
    archivoSQL.write(lineaSql)
    for tuplastransformadas in datos_a_insertar:
        lineaSql=str(tuplastransformadas)
        archivoSQL.write(lineaSql+", \n")
        print(lineaSql)
    archivoSQL.write(";;")
    archivoSQL.close()

consultaInsertEstacionClim = "INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion,situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# # Nombre de la tabla a truncar
# tabla = "Estacion_climatologica"

# # Consulta TRUNCATE TABLE
# consulta = f"TRUNCATE TABLE {tabla}"

# # Ejecutar la consulta
# cursor.execute(consulta)

# # Insertar los datos en lotes
cursor.executemany(consultaInsertEstacionClim, datos_a_insertar)
#La siguiente linea inserta en la bd
midb.commit()

archivo.close()
print("Se creo el archivo: Stations.sql")
