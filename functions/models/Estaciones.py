import mysql.connector

        # Configurar la conexión a la base de datos
class Estaciones:
    def __init__(self,num_estacion,nombre_estacion,municipio_id,situacion,organismo_id,latitud,longitud,altitud_msnm,emision_fecha):
        self.num_estacion=num_estacion
        self.nombre_estacion=nombre_estacion
        self.municipio_id=municipio_id
        self.situacion=situacion
        self.organismo_id=organismo_id
        self.latitud=latitud
        self.longitud=longitud
        self.altitud_msnm=altitud_msnm
        self.emision_fecha=emision_fecha

    def insert_row_to_table(fecha,precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id):
        if(fecha==None or precipitacion_mm==None or evaporacion_mm==None or tmax==None or tmin==None or humedad_relativa!=None or estacion_id==None):
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="psytranc3",
                database="climatologia_diaria"
            )
            cursor=conexion.cursor()
            query_insert = "INSERT INTO Datos_Climatologicos (fecha,precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            valores_insert = (f"{fecha},{precipitacion_mm},{evaporacion_mm},{tmax},{tmin},{humedad_relativa},{estacion_id}")
            cursor.execute(query_insert, valores_insert)
            conexion.commit()
        else:
            print("Te falta un campo")

