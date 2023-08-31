from datetime import datetime

def transform_FechaFormat(fecha_str):
    #print("transformando fecha")
    fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
    fecha_transformada = fecha_obj.strftime("%Y-%m-%d")
    return fecha_transformada