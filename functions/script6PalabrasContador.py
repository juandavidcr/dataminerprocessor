def contar_palabra_en_archivo(archivo_nombre, palabra_buscada):
    contador = 0
    with open(archivo_nombre, 'r') as archivo:
        for linea in archivo:
            palabras = linea.strip().split()  # Dividir la línea en palabras
            contador += palabras.count(palabra_buscada)

    return contador

archivo_nombre = "newfile.txt"
palabra_buscada = "ESTACION"
palabra_buscada1 = "MUNICIPIO"
palabra_buscada2 = "NOMBRE"
palabra_buscada3 = "ESTADO"
palabra_buscada4 = "EMISION"
palabra_buscada5 = "ORGANISMO"
contador = contar_palabra_en_archivo(archivo_nombre, palabra_buscada)
print(f'La palabra "{palabra_buscada}" aparece {contador} veces en el archivo.')
print(f'La palabra "{palabra_buscada1}" aparece {contador} veces en el archivo.')
print(f'La palabra "{palabra_buscada2}" aparece {contador} veces en el archivo.')
print(f'La palabra "{palabra_buscada3}" aparece {contador} veces en el archivo.')
print(f'La palabra "{palabra_buscada4}" aparece {contador} veces en el archivo.')
print(f'La palabra "{palabra_buscada5}" aparece {contador} veces en el archivo.')