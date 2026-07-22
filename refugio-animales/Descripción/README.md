
## Descripción

Este proyecto consiste en el diseño e implementación de una base de datos para la gestión de un refugio de animales, desarrollada utilizando SQL Server. A partir de un modelo lógico y físico se construyó una base de datos relacional que permite administrar la información de animales, visitantes, empleados, padrinos, donaciones, revisiones médicas y visitas al refugio. 

Además, se implementó un conjunto de reglas de negocio mediante triggers para garantizar la integridad de los datos y automatizar procesos del sistema, como la gestión de turnos, el registro de donaciones y las restricciones sobre las visitas a animales adoptados o fallecidos.   

Como complemento, se diseñó un Data Warehouse con un esquema Snowflake orientado al análisis multidimensional de la actividad del refugio. La tabla de hechos registra cada visita y se relaciona con dimensiones de tiempo, animales, visitantes, empleados y resultados, permitiendo generar indicadores para apoyar la toma de decisiones. 



## Conclusiones

Este proyecto permitió aplicar de manera práctica conceptos de modelado de datos, diseño de bases de datos relacionales y desarrollo de soluciones analíticas. A lo largo del trabajo se implementó una base de datos completa, respetando criterios de normalización, integridad referencial y reglas de negocio mediante triggers.

La construcción del Data Warehouse permitió transformar los datos operacionales en una estructura optimizada para el análisis, facilitando la obtención de métricas e indicadores relevantes, como tiempos de adopción, perfiles de visitantes, donaciones y actividad del refugio. 

En conjunto, el proyecto demuestra cómo integrar bases de datos transaccionales, automatización mediante SQL y técnicas de Business Intelligence para convertir datos en información útil para la gestión y la toma de decisiones.
