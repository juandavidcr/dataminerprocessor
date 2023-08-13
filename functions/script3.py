#!/usr/bin/env python
# decoding: utf-8
#
import re

from datetime import datetime

import mysql.connector

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
listaOrg=[]
listaEstaciones=[]
listaNombreEstaciones=[]
listaSituacion=[]
listaLat=[]
listaLon=[]
listaAlt=[]
listaEmision=[]
listaEmision2=[]
#dar formato de entrada de la base de datos
def createFecha(aaaa,mm,dd):
    fecha=date(int(aaaa),int(mm),int(dd))
    print(fecha)
    #return fecha
# ec_num_estacion=[]
cursor=midb.cursor()
# resultadoMunicipioId = 
#definicion de constantes
null=None
humedadRelativa=None
Estado_ID=30


archivo = open("./1_newfile.txt")
#definicion de lista de data 
i = 1

#lectura linea por linea encontrando el texto de interés y almacenandolo en una lista
for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    #print(listResult)
    if(listResult[0]=='LONGITUD'):
        listaLon.append(listResult[2])
        for i in range(len(listaLon)):
            listaLon2 = listaLon[i].replace("�","°")
            print(listaLon2)
    if(listResult[0]=='LATITUD'):
        listaLat.append(listResult[2])
        for i in range(len(listaLat)):
            listaLat2=listaLat[i].replace("�","°")
            print(listaLat2)
    if(listResult[0]=='ORGANISMO'):
        
        #select id_organismo from Organismo where nombre_org='CONAGUA-SMN';
        print("---organismo-list---")
        listaOrg.append(listResult[2])
        sqlOrgId=f"SELECT id_organismo FROM Organismo WHERE nombre_org like '{listaOrg[0]}'"
        cursor.execute(sqlOrgId)
        resultadoOrgId=cursor.fetchall()
        #valuesOrg = listaOrg[0]
        #cursor.execute(sqlOrgId)
        cleanidOrg = sqlSelectMunId.replace(",)", "")
        cleaningx2Org=cleanidOrg
        cleanedSQLOrg=cleaningx2Org.replace("(","")
        print(sqlOrgId)
        print("OrgId",resultadoOrgId)
    # Armar query de Estacion Climatologica
    if(listResult[0]=='MUNICIPIO'):
        sqlListMunNombre = "SELECT nombre_mun FROM Municipio;"
        cursor.execute(sqlListMunNombre)
        resultadoMunNombre=cursor.fetchall()
        numMunicipios = len(resultadoMunNombre)
        print("resultadoMunNombre: ",resultadoMunNombre)
        for j in range(numMunicipios):
            sqlSelectMunId="SELECT id_municipio FROM Municipio WHERE nombre_mun="+str(resultadoMunNombre[j])+";";
            cleaningx = sqlSelectMunId.replace(",)", "")
            cleaningx2=cleaningx
            cleanedSQL=cleaningx2.replace("(","")
            print(cleanedSQL)
            cursor.execute(cleanedSQL)
            resultadoMunId=cursor.fetchall()
            #numMunId=len(resultadoMunId)
            #print("Municipio Id: ",resultadoMunId)
            cleaningy1 = str(resultadoMunId).replace("[","",1)
            cleanedy2=cleaningy1.replace("(","")
            cleanedMunId=cleanedy2.replace(",)","",1)
            MunicipioIdCleaned=cleanedMunId.replace("]","",1)
            print("cleanedMunId: ",MunicipioIdCleaned)

        listaMun.append(listResult[2])
        print("Municipios: ",listaMun)
    if(listResult[0]=='ESTACION'):
        print("Existe Estacion")
        listaEstaciones.append(listResult[2])
        print("NumEstacion: ",listaEstaciones)
        num_estacion=0
        #for estacion in listaEstaciones:
        #estacion=Estaciones({listaEstaciones[i]},{listaNombreEstaciones[i]},MunicipioIdCleaned)
    if(listResult[0]=='NOMBRE'):
        n=len(listResult)
        print("Existe nombre-estacion: tam ---->",n)
        listaNombreEstaciones.append(f"{str(listResult[2])}{str(listResult[3])}")
        print("NOMBRE ESTACION: ",listaNombreEstaciones)
    if(listResult[0]=='ALTITUD'):
        listaAlt.append(listResult[2]+' '+listResult[3])
        print(listaAlt)
    if(listResult[0]=='EMISION'):
        listaEmision.append(listResult[2])
        fecha_str = listaEmision[0]  # Cambia esto por la fecha que quieras transformar
        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
        fecha_transformada = fecha_obj.strftime("%Y-%m-%d")
        #print(fecha_transformada)
        listaEmision2.append(fecha_transformada)
        print(listaEmision2)
    if(listResult[0]=='SITUACI�N'):
        listaSituacion.append(listResult[2])
        print("SITUACI�N: ",listaSituacion)
    listaDeEstaciones = [
        Estaciones(30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm','2020-04-06'),
        Estaciones(30452,'COATEPEC','OPERANDO',2,2,'019.508','-096.949','1,349 msnm','2020-04-06')
    ]
    
    i+=1
archivo.close()
