## Análisis exploratorio de datos (EDA)

Se realizó un análisis exploratorio detallado del dataset integrado, que combina variables meteorológicas (`tmin`, `tavg`, `tmax`, `wspd`, `prcp`, `pres`) con contaminantes del aire (`PM2.5`, `CO`, `SO2`). El objetivo fue identificar patrones que expliquen la ocurrencia de días con diferentes niveles de riesgo de contaminación atmosférica, clasificados según los umbrales de `PM10`.

### Gráficos incluidos:

- **Histogramas de distribución:**  
  Se generaron histogramas para visualizar la forma de la distribución de las variables numéricas. Permitieron detectar sesgos, concentraciones, y rangos típicos de valores. Por ejemplo:
  - `PM2.5` y `CO` mostraron distribuciones asimétricas, con una gran cantidad de valores bajos y pocos valores altos.
  - `wspd` (velocidad del viento) y `prcp` (precipitación) presentaron muchos valores cercanos a cero.

- **Boxplots por nivel de riesgo:**  
  Se utilizaron diagramas de caja para comparar la distribución de las variables clave (`PM2.5`, `CO`, `tmin`, `tavg`, `tmax`, `wspd`) entre los distintos niveles de riesgo (`Bajo`, `Medio`, `Alto`). Se observaron diferencias claras:
  - Los días con riesgo **‘Alto’** tendieron a registrar valores más altos de `PM2.5` y `CO`.
  - Las temperaturas mínimas (`tmin`) fueron más bajas en días con mayor riesgo, lo cual refuerza la hipótesis sobre el impacto de la calefacción en la contaminación.

- **Matriz de correlación:**  
  Se construyó una matriz de correlación para detectar relaciones lineales entre variables numéricas. Algunos hallazgos:
  - Correlación negativa entre temperatura y contaminantes: a menor temperatura, mayor nivel de polución.
  - Correlación positiva entre contaminantes: `PM2.5`, `CO` y `SO2` tienden a aumentar juntos.

### Estadísticas relevantes:

Se calcularon estadísticas descriptivas agrupadas por nivel de riesgo. Entre los resultados más destacados:
- El promedio de `PM2.5` en días de riesgo **‘Alto’** fue considerablemente mayor que en días de riesgo **‘Bajo’**.
- También se detectó menor velocidad del viento promedio en los días de riesgo **‘Alto’**, lo que sugiere acumulación de contaminantes por falta de dispersión.

Este análisis permitió seleccionar variables relevantes para el modelo predictivo, y fundamentar decisiones sobre el tratamiento de outliers y el preprocesamiento de datos.

## Conclusiones clave derivadas del análisis exploratorio

Del análisis exploratorio de datos surgieron hallazgos fundamentales que orientaron el diseño del modelo predictivo:

- **Las variables contaminantes se comportan de manera coordinada**: PM10, PM2.5 y CO muestran una correlación alta entre sí, lo que indica que los episodios de alta contaminación no se deben a un único contaminante, sino a una combinación.

- **El riesgo de contaminación se intensifica en condiciones meteorológicas específicas**:
  - Las temperaturas mínimas y medias son más bajas en días con riesgo ‘Alto’.
  - La velocidad del viento también disminuye, lo que favorece la acumulación de contaminantes en el aire.

- **La variable `PM10` fue utilizada únicamente para clasificar el nivel de riesgo**, y se excluyó como variable predictora para evitar filtración de información (`data leakage`) en el modelado.

- **Se observaron distribuciones asimétricas y valores extremos** (outliers) especialmente en CO, PM2.5 y precipitación. En lugar de eliminarlos, se aplicó un **tratamiento suave (winsorizing)** para preservar la clase ‘Alto’, que es crítica desde el punto de vista sanitario.

- El comportamiento diferenciado de las variables según el nivel de riesgo validó su **relevancia como predictores**, justificando su inclusión en el modelo de clasificación.

Estas conclusiones permiten afirmar que los datos disponibles contienen información significativa y estructurada para anticipar condiciones de riesgo ambiental, y que las variables seleccionadas son pertinentes tanto desde el punto de vista estadístico como ambiental.