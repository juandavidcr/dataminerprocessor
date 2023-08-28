nombre_archivo = "./datafile.txt"
#token = "fin"  # El token que estamos buscando
token = "--------------------------------------"

encontrado = False
numVecesEncontrado=0
# Leer el archivo línea por línea hasta encontrar el token
with open(nombre_archivo, 'r') as archivo:
    while not encontrado:
        linea = archivo.readline().strip()
        if not linea:  # Si no quedan más líneas
            break
        #print("Línea:", linea)
        if token in linea:
            numVecesEncontrado+=1
            encontrado = True

if encontrado:
    print(f"Token '{token}' encontrado. veces: {numVecesEncontrado}")
else:
    print(f"Token '{token}' no encontrado.")