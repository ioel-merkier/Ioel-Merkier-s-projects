# Código
El proyecto fue desarrollado en Python y está dividido en dos archivos principales para separar las funciones del programa de su ejecución.

# funciones.py
Este archivo contiene las funciones auxiliares utilizadas para leer, limpiar, transformar y ordenar los datos.
Entre sus principales tareas se encuentran:
- Leer archivos CSV.
- Extraer el año, mes y día de las fechas.
- Eliminar espacios y convertir textos a minúsculas.
- Filtrar columnas específicas.
- Ordenar listas de forma ascendente o descendente.
- Interpretar resultados de partidos, incluyendo definiciones por penales.
- Buscar la posición de una selección en el ranking FIFA.
- Identificar la confederación de cada país.
- Contar la cantidad de partidos disputados por cada capitán.
- Crear archivos de texto con los resultados obtenidos.

# main.py
Este archivo contiene las funciones principales del análisis y ejecuta el programa.
El análisis se divide en cuatro partes:
- Promedio de asistentes
- Calcula la cantidad promedio de espectadores de cada edición del Mundial y muestra los resultados ordenados por año.
- Batacazos
- Solicita al usuario un año y detecta partidos en los que una selección ubicada fuera del top 10 del ranking FIFA venció a una selección que estaba dentro de los primeros diez puestos.
- Victorias americanas
- Analiza los partidos de eliminación directa e identifica victorias de selecciones pertenecientes a CONMEBOL o CONCACAF frente a equipos de UEFA.
- Grandes leyendas
- Cuenta cuántas veces cada jugador representó a su selección como capitán y genera un archivo de texto con los capitanes que disputaron más partidos.
