def reemplazar_caracter_ultimo_linea_anterior(nombre_archivo):
    with open(nombre_archivo, 'r+') as archivo:
        lineas = archivo.readlines()
        if len(lineas) >= 2:
            linea_anterior = lineas[-2].rstrip('\n')
            ultima_linea = lineas[-1].rstrip('\n')
            if len(linea_anterior) > 0:
                #linea_anterior = linea_anterior[:-1] + ''  
                linea_anterior = linea_anterior[:-2] + ';'  # Reemplazar el último caracter por un punto y coma
                lineas[-2] = linea_anterior + '\n'
                archivo.seek(0)
                archivo.writelines(lineas)
                archivo.truncate()

# Nombre del archivo
nombre_archivo = "Data.sql"

# Llamada a la función
reemplazar_caracter_ultimo_linea_anterior(nombre_archivo)
print("Revisa tu nuevo archivo Data.sql si deseas insetar de manera manual. Fin ")
