# Análisis histórico de los Mundiales FIFA

Proyecto desarrollado en Python para analizar información histórica de los Mundiales de fútbol a partir de archivos CSV.

## Objetivos

El programa permite:

- Calcular el promedio de asistentes por edición.
- Detectar resultados inesperados según el ranking FIFA.
- Analizar victorias de selecciones americanas frente a equipos europeos.
- Identificar a los jugadores que participaron en más partidos como capitanes.
- Generar un archivo de texto con las grandes leyendas de los Mundiales.

## Tecnologías utilizadas

- Python
- Manejo de archivos CSV
- Procesamiento y limpieza de datos
- Funciones
- Listas
- Ordenamiento y filtrado de información

## Archivos del proyecto

```text
FIFA-mundiales-historico/
├── funciones.py
├── main.py
├── partidos.csv
├── ranking_fifa.csv
└── README.md
```

- `main.py`: contiene la ejecución principal del programa.
- `funciones.py`: contiene las funciones utilizadas para procesar los datos.
- `partidos.csv`: contiene información histórica de los partidos.
- `ranking_fifa.csv`: contiene las posiciones de las selecciones en el ranking FIFA.

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/ioel-merkier/Ioel-Merkier-s-projects.git
```

### 2. Entrar a la carpeta

```bash
cd Ioel-Merkier-s-projects/FIFA-mundiales-historico
```

### 3. Ejecutar el programa

```bash
python3 main.py
```

También puede ejecutarse con:

```bash
python main.py
```

El programa mostrará los resultados en la terminal y generará el archivo:

```text
grandes_leyendas.txt
```

## Autor

Ioel Merkier
