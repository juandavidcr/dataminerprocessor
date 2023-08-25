import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejemplo de datos para insertar (lista de tuplas)
datos_a_insertar = [
    ("valor1", "valor2"),
    ("valor3", "valor4"),
    # Agrega más tuplas según sea necesario
]

# Consulta de inserción con placeholders
consulta = "INSERT INTO tu_tabla (columna1, columna2) VALUES (%s, %s)"

# Insertar los datos en lotes
cursor.executemany(consulta, datos_a_insertar)

# Hacer commit para aplicar los cambios
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()