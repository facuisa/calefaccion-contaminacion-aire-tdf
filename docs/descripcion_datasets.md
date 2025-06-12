# Descripción de los Datasets

## 📄 pm10 coyhaique (extended).csv

- **Cantidad de instancias**: 21215
- **Cantidad de columnas**: 6
- **Columnas y tipos de datos:**
  - `FECHA (YYMMDD)`: `int64`
  - `HORA (HHMM)`: `int64`
  - `Registros validados`: `float64`
  - `Registros preliminares`: `float64`
  - `Registros no validados`: `float64`
  - `Unnamed: 5`: `float64 (sin contenido útil)`
- **Descripción:**
  Contiene registros horarios de concentraciones de material particulado PM10 en la ciudad de Coyhaique. La columna más relevante es 'Registros validados', que representa los valores aceptados oficialmente. Las demás columnas pueden contener datos preliminares, no validados o irrelevantes. Los datos están registrados con una frecuencia horaria. La columna 'Unnamed: 5' no contiene información útil.

## 📄 pm2.5 coyhaique..csv

- **Cantidad de instancias**: 21239
- **Cantidad de columnas**: 6
- **Columnas y tipos de datos:**
  `o	Igual que en el archivo de PM10.`
- **Descripción:**
  Contiene registros horarios de PM2.5 (material particulado fino) en Coyhaique. Al igual que el archivo de PM10, la columna 'Registros validados' es la principal fuente de información. Se presenta información complementaria sobre datos preliminares o no validados, pero en general estos campos están vacíos. 'Unnamed: 5' es una columna vacía.

## 📄 CO coyhaique.csv

- **Cantidad de instancias**: 21239
- **Cantidad de columnas**: 6
- **Columnas y tipos de datos:**
  - `FECHA (YYMMDD)`: `int64`
  - `HORA (HHMM)`: `int64`
  - `Registros validados`: `object (números como texto con coma decimal, ej. '0,25')`
  - `Registros preliminares`: `object`
  - `Registros no validados`: `object`
  - `Unnamed: 5`: `float64`
- **Descripción:**
  Contiene registros horarios de concentraciones de Monóxido de Carbono (CO) en Coyhaique. La columna principal es 'Registros validados', aunque los datos vienen en formato string con comas como separador decimal (por ejemplo, '0,25'), por lo que requiere preprocesamiento para convertirlos a valores numéricos. Las columnas de registros preliminares y no validados están mayormente vacías. 'Unnamed: 5' es una columna residual.

## 📄  SO2 coyahique.csv
- **Cantidad de instancias**: 21.239
- **Cantidad de columnas**: 6
- **Columnas y tipos de datos:**
  - `FECHA (YYMMDD)`: `int64`
  - `HORA (HHMM)`: `int64`
  - `Registros validados`: `object (valores tipo '1' como texto)`
  - `Registros preliminares`: `object`
  - `Registros no validados`: `float64`
  - `Unnamed: 5`: `float64`

- **Descripción:**
Contiene concentraciones horarias de Dióxido de Azufre (SO2). Similar a los archivos anteriores, los datos principales están en Registros validados, aunque vienen como texto y hay que convertirlos. Las columnas auxiliares están mayormente vacías.


## 📄 export (extended).csv (datos meteorológicos)

- **Cantidad de instancias**: 894
- **Cantidad de columnas**: 11
- **Columnas y tipos de datos:**
  - `date`: `object`
  - `tavg`: `float64`
  - `tmin`: `float64`
  - `tmax`: `float64`
  - `prcp`: `float64`
  - `snow`: `float64`
  - `wdir`: `float64`
  - `wspd`: `float64`
  - `wpgt`: `float64`
  - `pres`: `float64`
  - `tsun`: `float64`
- **Descripción:**
  Este archivo contiene variables meteorológicas diarias medidas en Coyhaique. Las variables incluyen temperatura media, mínima y máxima ('tavg', 'tmin', 'tmax'), precipitación ('prcp'), velocidad y dirección del viento ('wspd', 'wdir'), presión atmosférica ('pres') y horas de sol ('tsun'). La columna 'date' representa la fecha y requiere conversión a formato datetime. La mayoría de las columnas son de tipo float y algunas tienen valores nulos (como 'snow' o 'wpgt').

## 📄 umbrales_pm10.csv

- **Cantidad de instancias**: 3
- **Cantidad de columnas**: 3
- **Columnas y tipos de datos:**
  - `riesgo`: `object`
  - `pm10_min`: `int64`
  - `pm10_max`: `int64`
- **Descripción:**
  Tabla de referencia para clasificar los niveles de riesgo según los valores de PM10. Contiene tres niveles: Bajo, Medio y Alto, cada uno con un umbral mínimo y máximo ('pm10_min' y 'pm10_max'). Este archivo se utiliza para etiquetar o clasificar los días según el nivel de contaminación.

