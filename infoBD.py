
print(""" 
Esquemas: 
---------------------------------------------
DROP DATABASE IF EXISTS climatologia_diaria;
CREATE DATABASE climatologia_diaria;
USE climatologia_diaria;
CREATE TABLE Organismo(
    id_organismo int(10) NOT NULL AUTO_INCREMENT,
    nombre_org varchar(255),
    PRIMARY KEY (id_organismo)
);
CATALOGO ORGANISMO
INSERT INTO Organismo VALUES (1,'CONAGUA-SMN'),(2,'CONAGUA-DGE');

CREATE TABLE Estados_Republica_Mex(
id_estado int(5) NOT NULL AUTO_INCREMENT,
nombre_estado varchar(255)
);
CATALOGO DE ESTADOS DE LA REPUBLICA MEXICANA
INSERT INTO climatologia_diaria.Estados_Republica_Mex (id_estado,nombre_estado) VALUES
    (1,'Aguascalientes'),
    (2, 'Baja California'),
    (3, 'Baja California Sur'),
    (4, 'Campeche'),
    (5, 'Coahuila de Zaragoza'),
    (6, 'Colima'),
    (7, 'Chiapas'),
    (8, 'Chihuahua'),
    (9, 'Distrito Federal'),
    (10, 'Durango'),
    (11, 'Guanajuato'),
    (12, 'Guerrero'),
    (13, 'Hidalgo'),
    (14, 'Jalisco'),
    (15, 'México'),
    (16, 'Michoacán de Ocampo'),
    (17, 'Morelos'),
    (18, 'Nayarit'),
    (19, 'Nuevo León'),
    (20, 'Oaxaca de Juárez'),
    (21, 'Puebla'),
    (22, 'Querétaro'),
    (23, 'Quintana Roo'),
    (24, 'San Luis Potosí'),
    (25, 'Sinaloa'),
    (26, 'Sonora'),
    (27, 'Tabasco'),
    (28, 'Tamaulipas'),
    (29, 'Tlaxcala'),
    (30, 'Veracruz de Ignacio de la Llave'),
    (31, 'Yucatán'),
    (32, 'Zacatecas');

CREATE TABLE Municipio(
    id_municipio int(10) NOT NULL AUTO_INCREMENT,
    estado_id int(5),
    nombre_mun varchar(255),
    PRIMARY KEY (id_municipio),
    FOREIGN KEY (estado_id) REFERENCES Estados_Republica_Mex(id_estado)
);
INSERT INTO `Municipio` VALUES (1,30,'ATZALAN'),(2,30,'COATEPEC'),(3,30,'CHICONTEPEC'),(4,30,'COATEPEC 2'),(5,30,'CORDOBA'),(6,30,'HUATUSCO'),(7,30,'SAN ANDRES TUXTLA'),(8,30,'SANTIAGO TUXTLA'),(9,30,'SAN ANDRES TUXTLA 2'),(10,30,'SANTIAGO TUXTLA 2'),(11,30,'MISANTLA'),(12,30,'PAPANTLA'),(13,30,'TEZONAPA'),(14,30,'TEZONAPA 2'),(15,30,'ZONGOLICA');
      
DROP TABLE IF EXISTS Estacion_climatologica; 
#SE VA LLENAR DEPENDIENDO DE ID MUNICIPIO Y ID ORGANISMO
CREATE TABLE Estacion_climatologica (
    id_estacion int(20) NOT NULL AUTO_INCREMENT ,
    num_estacion varchar(50),
    nombre_estacion varchar(255),
    situacion varchar(255),
    municipio_id int(10),
    organismo_id int(10),
    latitud varchar(50),
    longitud varchar(50),
    altitud_msnm varchar(50),
    emision_fecha DATE,
    PRIMARY KEY (id_estacion),
    FOREIGN KEY (municipio_id) REFERENCES Municipio(id_municipio),
    FOREIGN KEY (organismo_id) REFERENCES Organismo(id_organismo)
);

CREATE TABLE Datos_Climatologicos(
    # id_climatologicos int(10) NOT NULL AUTO_INCREMENT,
    # fecha DATE,
    # precipitacion_mm FLOAT(5,1),
    # evaporacion_mm FLOAT(5,1),
    # tmax FLOAT(3,1),
    # tmin FLOAT(3,1),
    # humedad_relativa FLOAT(4,2),
    # estacion_id int(20),
    # PRIMARY KEY (id_climatologicos),
    # FOREIGN KEY (estacion_id) REFERENCES Estacion_climatologica(id_estacion)
 );   
 """)
