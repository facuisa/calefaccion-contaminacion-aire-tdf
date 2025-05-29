
# Descripción de Datasets

Este documento resume las características de los datasets utilizados en el proyecto de predicción de contaminación atmosférica en Tierra del Fuego.

---

## 1. `atmpm10_2023_nuevo.csv`
- **Instancias**: 12
- **Columnas**: Tabla resumen de PM10 por estaciones
- **Tipo de datos**: `object`
- **Descripción**: Contiene valores anuales promedio de PM10 (material particulado) registrados por distintas estaciones de monitoreo.
- **Uso**: Análisis exploratorio preliminar.

---

## 2. `15_3_05_Gas_natural_red_Consumo.xlsx`
- **Instancias**: 7
- **Columnas**: Año y consumo por tipo de usuario
- **Tipo de datos**: `object`
- **Descripción**: Datos de consumo de gas natural por red en Tierra del Fuego, por tipo de usuario.
- **Uso**: Evaluación del uso de energía no eléctrica como posible indicador de calefacción.

---

## 3. `15_3_06_Gas_natural_red_Usuarios.xlsx`
- **Instancias**: 38
- **Columnas**: Año, categoría de usuario, cantidad de usuarios
- **Tipo de datos**: `float64`, `object`
- **Descripción**: Número de usuarios conectados a la red de gas por categoría, desde 1993 a 2023.
- **Uso**: Análisis de cobertura del sistema de calefacción por gas.

---

## 4. `15_3_01_Energia_electrica_consumida_por_tipo_usuario.xlsx`
- **Instancias**: 14
- **Columnas**: Año y consumo por tipo de usuario
- **Tipo de datos**: `object`
- **Descripción**: Consumo eléctrico anual desagregado por tipo de usuario en Ushuaia, Río Grande y Tolhuin.
- **Uso**: Relación entre consumo eléctrico y demanda de calefacción.

---

## 5. `datohorario20250527.txt`
- **Instancias**: 2185
- **Columnas**: `FECHA`, `HORA`, `TEMP`, `HUM`, `PNM`, `DD`, `FF`, `NOMBRE`
- **Tipo de datos**: `object`, `float64`
- **Descripción**: Datos meteorológicos horarios, incluyendo temperatura, humedad, presión, dirección y velocidad del viento.
- **Uso**: Variables predictoras clave para modelos de calidad del aire.

---

## 6. `registro_temperatura365d_smn.txt`
- **Instancias**: 42924
- **Columnas**: `FECHA`, `TMAX`, `TMIN`, `NOMBRE`
- **Tipo de datos**: `object`, `float64`
- **Descripción**: Registro de temperaturas máximas y mínimas diarias de múltiples estaciones meteorológicas del país.
- **Uso**: Identificación de patrones térmicos estacionales, correlación con eventos de contaminación.

---
