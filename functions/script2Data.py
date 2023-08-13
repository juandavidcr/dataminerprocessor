import re
from datetime import date

#Buscamos en el archivo de cabaceras en este caso newfile.txt y encontrar patrones de escritura y cuantas palabras hay en una linea
filename = 'newfile.txt'
with open(filename) as file_obj:
    # for line in file_obj:
    #     print(line.rstrip())
    lines = file_obj.readlines()
    
for line in lines:
    listaPalabras = line.split()
    nPal=len(listaPalabras)
    frecuenciaPalab = []
    for w in listaPalabras:
        frecuenciaPalab.append(listaPalabras.count(w))
    print("nPal: "+str(nPal))
    print("Cadena\n" + line +"\n")
    print("Lista\n" + str(listaPalabras) + "\n")
    print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
    print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
    print(line)

# exStr = """ESTACION  : 30012
# NOMBRE    : ATZALAN
# ESTADO    : VERACRUZ DE IGNACIO DE LA LLAVE
# MUNICIPIO : ATZALAN
# SITUACI�N : OPERANDO
# ORGANISMO : CONAGUA-SMN
# CVE-OMM   : Nulo
# LATITUD   : 019.789�
# LONGITUD  : -097.246�
# ALTITUD   : 1,697 msnm
 
# EMISION   : 06/04/2020"""
# linea = re.split(r'\s+\:+\n*', exStr)

# # print(linea[0])
# # print(linea[1])
# # print(linea[2])

# # print(linea[3])
# # print(linea[4])
# # print(linea[5])

# # print(linea[6])
# # print(linea[7])
# # print(linea[8])
# # print(linea[9])
# # print(linea[10])
# print(linea[11])
# #print(len(linea))
# def createDate(datos):
#     date = re.split(r'\/',datos)
#     for daymonthyear in range[len(date)]:
#         print(daymonthyear)
# createDate(linea[11])
# #fecha = 
# #print(fecha)

