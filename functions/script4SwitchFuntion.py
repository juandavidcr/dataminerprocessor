def case_6():
    return "Caso 0 seleccionado."

def case_5():
    return "Caso 1 seleccionado."

def case_4():
    return "Caso 2 seleccionado."

def case_3():
    return "Caso 2 seleccionado."

def default_case():
    return "Opción no válida."

def switch_case(case):
    switch_dict = {
        6: case_6,
        5: case_5,
        4: case_4,
        3: case_3
    }
    return switch_dict.get(case, default_case)()

# Cambia el valor de 'selected_case' para probar diferentes casos
selected_case = 1
result = switch_case(selected_case)
#print(result)

def convertTuple(tup):
    
    return
 
# Driver code
tuple = [(6,)]
string = convertTuple(tuple)
string.replace(",)","")
print(string)