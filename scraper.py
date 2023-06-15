from selenium import webdriver
from bs4 import BeautifulSoup
import json
import psycopg2

# Configurar Selenium para usar Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo sin cabeza
driver = webdriver.Chrome(options=options)

# Obtener la página web
url = 'https://snifa.sma.gob.cl/Sancionatorio/Resultado'
driver.get(url)

# Obtener el contenido HTML de la página
html = driver.page_source

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Obtener la tabla
tabla = soup.find('table')
filas = tabla.find_all('tr')

# Obtener los encabezados de cada columna
encabezados = []
cabeceras = tabla.find_all('th')
for cabecera in cabeceras:
    encabezados.append(cabecera.text.strip())

# Obtener los datos de la tabla
datos = []
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fila_datos = [celda.text.strip() for celda in celdas]
        datos.append(fila_datos)

# Cerrar el navegador
driver.quit()

# Combinar los encabezados con los datos en un diccionario
registros = []
for fila_datos in datos:
    registro = dict(zip(encabezados, fila_datos))
    registros.append(registro)

# Guardar los datos en un archivo JSON
with open('datos.json', 'w') as archivo:
    json.dump(registros, archivo, indent=4)

print("Datos guardados en el archivo datos.json")

# Cargar los datos desde el archivo JSON
with open('datos.json') as archivo:
    registros = json.load(archivo)

# Establecer la conexión a la base de datos
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='testCHC',
    user='postgres',
    password='1234'
)

# Crear la tabla en la base de datos si no existe
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        expediente TEXT PRIMARY KEY,
        unidad_fiscalizable TEXT,
        nombre_razon_social TEXT,
        categoria TEXT,
        region TEXT,
        estado TEXT,
        detalle TEXT
    )
''')
conn.commit()

# Recorrer los registros y guardar en la base de datos
for registro in registros:
    try:
        cursor.execute('''
            INSERT INTO registros (expediente, unidad_fiscalizable, nombre_razon_social, categoria, region, estado, detalle)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (expediente) DO UPDATE
            SET unidad_fiscalizable = excluded.unidad_fiscalizable,
                nombre_razon_social = excluded.nombre_razon_social,
                categoria = excluded.categoria,
                region = excluded.region,
                estado = excluded.estado,
                detalle = excluded.detalle
        ''',
        (registro['Expediente'], registro['Unidad Fiscalizable'], registro['Nombre razón social'],
        registro['Categoría'], registro['Región'], registro['Estado'], registro['Detalle']))
        conn.commit()
        print(f"Registro '{registro['Expediente']}' guardado o actualizado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al guardar el registro '{registro['Expediente']}': {e}")

# Cerrar la conexión a la base de datos
conn.close()
