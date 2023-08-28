nombre_archivo = "./datafile.txt"
#token = "token"
token = "--------------------------------------"

numero_tokens_objetivo = 15
secciones = []

# Contar el número de tokens
contador_tokens = 0
with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
        contador_tokens += linea.count(token)
        if contador_tokens >= numero_tokens_objetivo:
            break

# Leer secciones divididas por los tokens
with open(nombre_archivo, 'r') as archivo:
    seccion_actual = []
    for linea in archivo:
        seccion_actual.append(linea)
        if token in linea:
            secciones.append(seccion_actual)
            seccion_actual = []

# Imprimir secciones encontradas
for i, seccion in enumerate(secciones, start=1):
    print(f"Sección {i}:")
    for linea in seccion:
        print(linea.strip())
    #print("-" * 20)
