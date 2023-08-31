import re
from datetime import date

#Buscamos en el archivo de cabaceras en este caso newfile.txt y encontrar patrones de escritura y cuantas palabras hay en una linea
filename = 'newfile.txt'
with open(filename) as file_obj:
    
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
