class DataClimatologiaDiaria:
    def __init__(self,id_climatologicos,fecha,precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id):
        self.id_climatologicos=id_climatologicos
        self.fecha=fecha
        self.precipitacion=precipitacion_mm
        self.evaporacion=evaporacion_mm
        self.tmax=tmax
        self.tmin=tmin
        self.humedad_rel=humedad_relativa
        self.estacion_id=estacion_id
