## Análisis de Ventas de Automóviles

## Descripción del trabajo
El presente trabajo consiste en el desarrollo de un tablero interactivo en Power BI orientado al análisis comercial de una red de concesionarias de automóviles. El objetivo es transformar datos transaccionales de ventas en información útil para la toma de decisiones, permitiendo identificar patrones de comportamiento comercial a lo largo de dos años de operación (2022–2023).
El modelo de datos subyacente sigue un esquema de estrella, compuesto por una tabla de hechos y cuatro tablas de dimensión:
Fact_Ventas: registra cada operación de venta (23.906 registros), con fecha, vehículo, cliente, distribuidor y precio.
Dim_Auto: catálogo de 740 vehículos, con marca, modelo, motor, transmisión, color y tipo de carrocería.
Dim_Clientes: 3.022 clientes, con género e ingreso anual.
Dim_Dealer: 196 distribuidores, agrupados por región geográfica.
Dim_Fechas: tabla calendario para el análisis temporal de las ventas.
El reporte se estructura en cinco páginas: un Menú Principal de navegación, y cuatro páginas analíticas (General, Marcas y Autos, Dealers y Clientes), cada una con indicadores clave (KPIs), gráficos de evolución temporal, comparativas por categoría (marca, modelo, región, carrocería) y filtros interactivos (año, marca, región) que permiten al usuario explorar los datos desde distintas perspectivas.

## Principales hallazgos
Volumen y facturación general
Se registraron 23.906 operaciones entre enero de 2022 y diciembre de 2023, por un total de $671.525.465, con un ticket promedio de $28.090 por venta.
Marcas
Chevrolet, Dodge y Ford concentran el mayor volumen de unidades vendidas, y son también las marcas líderes en facturación, superando cada una los $44 millones.
El liderazgo en unidades no siempre coincide con el de precio promedio, lo que indica que la facturación depende tanto del volumen como del posicionamiento de precio de cada marca.
Distribuidores y regiones
Austin, Janesville y Scottsdale son las regiones con mayores ingresos, todas por encima de los $95 millones, mostrando una concentración geográfica relevante del negocio.
El desempeño entre los 196 distribuidores es heterogéneo: los tres principales (Rabun Used Car Sales, Progressive Shippers Cooperative y U-Haul CO) superan individualmente los $35 millones en ventas.
Producto
El tipo de carrocería más vendido es SUV (6.374 unidades), seguido de cerca por Hatchback (6.128), lo que refleja la preferencia del mercado por vehículos utilitarios y compactos por sobre el sedán tradicional (4.488 unidades).
Perfil de clientes
El 76% de las operaciones corresponden a clientes de género masculino (18.166) frente a un 24% femenino (5.740), evidenciando una fuerte asimetría en la base de compradores.
No se observa relación entre el ingreso anual del cliente y el precio del vehículo adquirido (correlación prácticamente nula, 0,004), lo que sugiere que la decisión de compra no está determinada linealmente por el poder adquisitivo declarado.

## Conclusiones
El análisis permite concluir que el negocio presenta una base sólida y diversificada de ventas, pero con oportunidades claras de mejora en la concentración comercial. La dependencia de un grupo reducido de marcas, regiones y distribuidores para gran parte de la facturación total representa tanto una fortaleza (marcas consolidadas y de alta rotación) como un riesgo (baja diversificación geográfica y de cartera).
La fuerte preferencia por SUV y Hatchback frente a otras carrocerías sugiere que las estrategias de stock, marketing y negociación con proveedores deberían priorizar estos segmentos, sin descuidar el resto del catálogo.
La marcada desproporción de género entre los compradores (76% masculino) abre una oportunidad de negocio: desarrollar acciones comerciales específicas para ampliar la participación del público femenino, actualmente subrepresentado.
Finalmente, la ausencia de correlación entre ingreso anual y precio de compra indica que el ingreso declarado no es, por sí solo, un buen predictor del ticket de venta, por lo que sería recomendable incorporar otras variables (edad, historial crediticio, tipo de financiación) para segmentar mejor a los clientes en futuros análisis.
En conjunto, el tablero desarrollado cumple su objetivo de convertir datos crudos de ventas en información accionable, brindando una base sólida para el diseño de estrategias comerciales orientadas por datos.


