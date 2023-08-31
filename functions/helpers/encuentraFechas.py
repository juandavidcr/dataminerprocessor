from datetime import datetime
import re
def encuentraFechas(fecha_str):
    patron_fecha = r'\b\d{2}/\d{2}/\d{4}\b'
    fechas_encontradas = re.findall(patron_fecha, fecha_str)
    if fechas_encontradas==None:
        return None
    fecha_obj = datetime.strptime(fechas_encontradas, "%d/%m/%Y")
    fecha_transformada = fecha_obj.strftime("%Y-%m-%d")
    return fecha_transformada