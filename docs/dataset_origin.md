# Informe sobre el Origen de los Datasets

Este proyecto utiliza diversas fuentes públicas y oficiales para construir un modelo predictivo de riesgo de contaminación del aire en Tierra del Fuego, Argentina, utilizando datos de Coyhaique, Chile, por su similitud climática. A continuación, se describen las fuentes, métodos de adquisición y características generales de cada dataset.

---

## 1. Datos de Contaminantes Atmosféricos  
**Archivos involucrados**:  
- `pm 10 coyhaique (extended).csv`  
- `pm 2.5 coyhaique.csv`  
- `CO coyhaique.csv`  
- `SO2 coyahique.csv`

- **Fuente**: Sistema Nacional de Información de Calidad del Aire (SINCA) – Chile  
- **Enlace**: [https://sinca.mma.gob.cl/index.php/estacion/index/id/264](https://sinca.mma.gob.cl/index.php/estacion/index/id/264)  
- **Fecha de adquisición**: junio de 2025  
- **Método de adquisición**: descarga directa desde el portal oficial, seleccionando la estación Coyhaique.  
- **Descripción**: Archivos en formato CSV que contienen registros horarios de concentraciones de PM10, PM2.5, CO y SO2 en microgramos por metro cúbico, incluyendo columnas para datos validados, preliminares y no validados.

---

## 2. Datos Meteorológicos  
**Archivo involucrado**:  
- `export (extended).csv`

- **Fuente**: Meteostat  
- **Enlace**: [https://meteostat.net/en/station/85864?t=2024-06-07/2025-06-07](https://meteostat.net/en/station/85864?t=2024-06-07/2025-06-07)  
- **Fecha de adquisición**: junio de 2025  
- **Método de adquisición**: exportación directa desde la plataforma Meteostat para la estación Coyhaique.  
- **Descripción**: Datos meteorológicos diarios que incluyen variables como temperatura media, máxima y mínima, precipitación, viento, presión y horas de sol. Los datos fueron descargados en formato CSV y no se modificaron al momento de la adquisición.

---

## 3. Datos de Calidad del Aire vía API  
**Archivo involucrado**:  
- `openaq_location_73_measurments.csv` (no incluido pero consultado como referencia cruzada)

- **Fuente**: OpenAQ  
- **Enlace**: [https://explore.openaq.org/locations/73](https://explore.openaq.org/locations/73)  
- **Método de adquisición**: consulta mediante API con autenticación (API Key).  
- **Descripción**: Este recurso fue utilizado para verificar valores de PM2.5 y PM10 y comparar mediciones con el portal SINCA. No forma parte del dataset final pero fue útil como fuente secundaria.

---

## 4. Tabla de Umbrales de Riesgo  
**Archivo involucrado**:  
- `umbrales_pm10.csv`

- **Fuente**: Elaboración propia basada en normativas internacionales de calidad del aire  
- **Referencia principal**: OMS (Organización Mundial de la Salud) y valores adoptados por el Ministerio del Medio Ambiente de Chile (SINCA)  
- **Descripción**: Tabla de clasificación de riesgo con tres categorías (Bajo, Medio, Alto), construida para el modelo predictivo. Los rangos utilizados son consistentes con los valores umbral de PM10 considerados por la normativa chilena:  
  - Bajo: 0–44 µg/m³  
  - Medio: 45–149 µg/m³  
  - Alto: 150 µg/m³ o más  

---

## Consideraciones Generales

- Todos los archivos fueron almacenados inicialmente en la carpeta `data/raw/`.
- En los contaminantes `CO` y `SO2`, los valores estaban expresados con coma como separador decimal y debieron ser transformados para su análisis.
- Los datos meteorológicos incluyen algunas columnas con valores nulos (`snow`, `wpgt`), que fueron considerados en el preprocesamiento.
- La tabla de umbrales fue generada por el equipo a partir de fuentes verificadas para facilitar la clasificación automática de los niveles de riesgo diario.

---