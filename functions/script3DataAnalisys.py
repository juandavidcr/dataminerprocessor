#!/usr/bin/env python
# decoding: utf-8
#
import mysql.connector
import re
#from datetime import datetime,date
from helpers.dateFormater import transform_FechaFormat
#from functions.models import 
from models.Estaciones import Estaciones

midb =mysql.connector.connect(
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
null=None
humedadRelativa=None
Estado_ID=30
archivo = open("./1_newfile.txt","r")

i = 1
for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    #listResult=re.split(r':', linea) 
    print(listResult)
    if(listResult[0]=='LONGITUD'):
        listaLon.append(listResult[2])
        for i in range(len(listaLon)):
            listaLon2 = listaLon[i].replace("�","°")
            print("LISTA LONG--->",listaLon2)
    if(listResult[0]=='LATITUD'):
        listaLat.append(listResult[2])
        for i in range(len(listaLat)):
            listaLat2=listaLat[i].replace("�","°")
            print("LISTA LAT----->",listaLat2)
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
        print("------------> numero de municipios: ",numMunicipios)
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
            
            print("cleanedSQL____________->",cleanedSQL)
            print("Municipio Id: ",resultadoMunId)
    if(listResult[0]=='ESTACION'):
        print("Existe Estacion")
        listaEstaciones.append(listResult[2])
        num_estacion=0       
    if(listResult[0]=='NOMBRE'):
        n=len(listResult)
        print("Existe nombre-estacion: tam ---->",n)
        listaNombreEstaciones.append(f"{str(listResult[2])} {str(listResult[3])} ")
        
    if(listResult[0]=='ALTITUD'):
        listaAlt.append(listResult[2]+' '+listResult[3])
    if(listResult[0]=='EMISION'):
        listaEmision.append(listResult[2])
        fecha_str = listaEmision[0]  
        dateOfDataWeather=transform_FechaFormat(fecha_str)        
        listaEmision2.append(dateOfDataWeather)
    if(listResult[0]=='SITUACI�N'):
        listaSituacion.append(listResult[2])
        i+=1
    
print("---------> cleanedMunId: ",MunicipioIdCleaned)
#print(" lMunID: --------->",listaMunId)
print("resultado ---> Municipio Nombre: ",resultadoMunNombre)
print("Numero de Estacion: ",listaEstaciones)
print("NOMBRE ESTACION: ",listaNombreEstaciones)
print("LISTA ALTITUD: ",listaAlt)
print("SITUACI�N: ",listaSituacion)
print("lista EMISION--> ",listaEmision2)
#print("LISTA ORGANIZAION ID------>",listaOrg)
#print("Municipios: lista----------->",listaMun)
print("OrgIds Lista:------>",listaIdorgNum)
x=0
datos_a_insertar = [
    (listaEstaciones[x],listaNombreEstaciones[x],listaSituacion[x],listaMunId[x],int(listaIdorgNum[x]),'019.789','-097.246','1,697 msnm','2020-04-06'),
    ('30452','COATEPEC','OPERANDO',2,2,'019.508','-096.949','1,349 msnm','2020-04-06')
]
#datos_a_insertar=[
    # ("valor1", "valor2"),
    # ("valor3", "valor4"),
    # # Agrega más tuplas según sea necesario
# ]

#datos_a_insertar.append()
# Consulta de inserción con placeholders
#INSERT INTO climatologia_diaria.Estacion_climatologica (num_estacion, nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES ('1', 'a', 'a', '1', '1', '123', '-123', '123', '2023-08-24');

consultaInsertEstacionClim = "INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion,situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# # Insertar los datos en lotes
cursor.executemany(consultaInsertEstacionClim, datos_a_insertar)
# #
#lineaNuevaSQL=f"""INSERT INTO Estacion_climatologica VALUES 
#(1,'30012','ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm','2020-04-06'),
#(2,'30452','COATEPEC','OPERANDO',2,2,'019.508','-096.949','1,349 msnm','2020-04-06');
#"""

archivo.close()

