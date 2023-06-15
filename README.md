
# Scraping de Información Sancionatoria Ambiental

Este proyecto consiste en desarrollar un script en Python para obtener la información presentada en la tabla de la página web https://snifa.sma.gob.cl/Sancionatorio/Resultado. El objetivo es realizar un scraping de los datos y almacenarlos en una base de datos PostgreSQL para su posterior consulta y análisis.

## Características


Utiliza Selenium y BeautifulSoup para realizar el scraping de la página web y extraer la información de la tabla.
Guarda los datos obtenidos en un archivo JSON para su posterior procesamiento.
Configura y utiliza una base de datos PostgreSQL para almacenar los registros obtenidos.
Permite establecer una conexión a la base de datos y crear la tabla necesaria para almacenar los datos.
Inserta los registros obtenidos en la base de datos, evitando duplicados mediante una cláusula ON CONFLICT.


## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias del proyecto:
   ```
  
3. Ejecuta python scraper.py
 
 

## Uso
- Asegúrate de tener una instancia de PostgreSQL en funcionamiento y configura los parámetros de conexión en el script scraper.py. Puedes modificar los valores de host, port, database, user y password en la sección correspondiente del código.
- Ejecuta el script scraper.py mediante el siguiente comando:  python scraper.py
- Verifica que los datos se hayan guardado correctamente en la base de datos PostgreSQL.


## Contribución

Si quieres contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama con tus cambios:
   ```
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus modificaciones y realiza commits descriptivos.
4. Envía un pull request explicando tus cambios y mejoras.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

## Autor

jose chirinos - josechirinos11@gmail.com
