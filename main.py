# import mysql.connector

from functions.script1DataCleanUp import getInfoDataTable,getInfoData,printlineas
from pexpect import EOF

#Dividir datos por cada estacion metereologica

#Obtener los organismos, municipios y estados llenar catalogos

#Obtener todas las estaciones metereologicas
# midb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='psytranc3',
#     database='climatologia_diaria',
#     auth_plugin='mysql_native_password'
# )

archivo = open("./bancdata/atzalan/atzalan.txt","r")

#sql = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#valuesMet = (30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm',date(2020,4,6))
#valuesMet = (30452,'COATEPEC','OPERANDO',2,2,'019.508','-096.949','1,349 msnm',date(2020,4,6))
#cursor=midb.cursor()
#cursor.execute(sql, valuesMet)
#almacenamiento de rutas 


#armado de rutas
directorio = "./bancdata/"
routeF = directorio+"atzalan/atzalan.txt"
routeF2 = directorio+"briones/briones.txt"
routeF3 = directorio+"chicontepec/chicontepec.txt"
routeF4 = directorio+"coatepec/coatepec.txt"
routeF5 = directorio+"cordoba/cordoba.txt"
routeF6 = directorio+"huatusco/huatusco.txt"
routeF7 = directorio+"los-tuxtlas/san-andres.txt"
routeF8 = directorio+"los-tuxtlas/santiago-tuxtla.txt"
routeF9 = directorio+"los-tuxtlas/sihuapan.txt"
routeF10 = directorio+"los-tuxtlas/tapalapa.txt"
routeF11 = directorio+"misantla/misantla.txt"
routeF12 = directorio+"papantla/papantla.txt"
routeF13 = directorio+"tezonapa/tezonapa-1.txt"
routeF14 = directorio+"tezonapa/tezonapa-2.txt"
routeF15 = directorio+"zongolica/zongolica.txt"

#almacenamiento de rutas 
listaData = [routeF,routeF2,routeF3,routeF4,routeF5,routeF6,routeF7,routeF8,routeF9,routeF10,routeF11,routeF12,routeF13,routeF14,routeF15]

#printlineas(listaData[0])
#getInfoDataTable(listaData[0])
#getInfoData(listaData[0])

for x in listaData:
    getInfoDataTable(x)
    getInfoData(x)