Script de Extracción de Información para proyecto de Roya Cafetales
--------------------------------------------------------------------
# Data Mining for Roya project (UAM CUAJIMALPA social service) from Google Earth
## _Documentación_
Descargar las BD de los municipios de Veracruz
De la liga: https://smn.conagua.gob.mx/tools/RESOURCES/estacion/EstacionesClimatologicas.kmz    
Descargar Google Earth y abrir el archivo kmz con el Google Earth.

Descargar los datos de cada municipio desde 2010 a la actualidad (y desde antes si hay esos datos disponibles).

- Coatepec
- Zongolica
- Tezonapa
- Córdoba
- Huatusco
- Briones
- Atzalan
- Misantla
- Papantla
- Chicontepec
- Los Tuxtlas

| Pasos | README | Ejemplo |
| -- | ---- | ------------- |
| 1 | Instalar las dependencias:  | pip install mysql-connector-python|
| 2 | Instalar python y Mysql | python3 y mysql8 |
| 3 | Cargar las bases de datos db.sql es donde se encuentra el esquema de las tablas es decir el esquema de las tablas y la bd| cargar catalogos de Organismos, Municipio y Estados_Republica_Mex|
| 4 | Catalogo de estados de la republica esta en el archivo  | Cargar en la bd dbestados.sql |
| 5 | Cargar en la carpeta bancdata los archivos recolectados de Google Earth | Los archivos estan dentro de la carpeta bancdata separados por municipio. |
| 6 | Correr el script main de python. El cual extrae la información de los archivos de los municipios de las carpetas donde se lee la información | Resultado genera 2 archivos que el usuario desea procesar uno con las cabeceras y otro con los datos de un municipio dependiendo del idMunicipio |
| 7 | Si se escoge la opcion 1 se debe escoger un nombre único para cada experimentación ya que si se corre el mismo nombre duplicará el numero de datos encontrados dentro del archivo nombrado por el usuario | Regresa un archivo de Stations.sql con la información de la estación climatológica y si el commit esta habilitado inserta en la base dedatos |
| 8 | Archivo 1  contiene información de las estaciones climatologicas y las dependencias gubernamentales de donde se extrae la información al igual que latitud y longitud para llenar las tablas Estacion_climatologica. | Seguir las instrucciones del programa|
| 9 | Si se escoge el Archivo 2  el script8 leera y creara un archivo de texto tipo sql con la data de la estacion climatologica y el id de Municipio y si esta habilitado el commit insertara los datos en la BD si es que se tiene una conexion a la BD| Si se escoge la opcion 1 o 2 procesa los archivos pero deberas volver a correr main para procesar la fase de ingesta ya sea para las 2 tablas disponibles hasta el momento de esta version de programa.|
