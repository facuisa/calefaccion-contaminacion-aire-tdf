
# Informe sobre el Origen del Dataset

Este proyecto utiliza múltiples fuentes de datos de dominio público y gubernamental para la construcción de un modelo predictivo de riesgo de contaminación del aire en Tierra del Fuego, Argentina. A continuación se detallan las fuentes, fechas de adquisición y procesos de obtención realizados.

---

## 1. Calidad del Aire (`atmpm10_2023_nuevo.csv`)
- **Fuente**: https://datos.gob.ar (datos recopilados por estaciones locales de monitoreo).
- **Fecha de adquisición**: mayo de 2025.
- **Método de adquisición**: Navegación directa en el portal correspondiente y descarga del archivo relacionado con el proyecto.
- **Descripción**: Contiene promedios de concentración de material particulado PM10 registrados durante 2023 por estación.

---

## 2. Consumo de Gas Natural y Electricidad  
**Archivos involucrados**:
- `15_3_05_Gas_natural_red_Consumo.xlsx`  
- `15_3_06_Gas_natural_red_Usuarios.xlsx`  
- `15_3_01_Energia_electrica_consumida_por_tipo_usuario.xlsx`

- **Fuente**: Instituto Provincial de Análisis e Investigación, Estadísticas y Censos (IPIEC) – Gobierno de Tierra del Fuego.
- **Fecha de adquisición**: mayo de 2025 desde el portal oficial (https://ipiec.tierradelfuego.gob.ar)
- **Método de adquisición**: Navegación directa en la sección de energía del IPIEC y descarga de archivos relacionados.
- **Descripción**: Datos históricos sobre consumo energético por tipo de usuario y categoría en Tierra del Fuego.

---

## 3. Datos Meteorológicos Horarios (`datohorario20250527.txt`)
- **Fuente**: Servicio Meteorológico Nacional (SMN) https://smn.gob.ar/
- **Método de adquisición**: Navegación directa en el sitio del SMN y descarga del archivo relacionado.
- **Descripción**: Registros por hora de variables como temperatura, humedad, presión, viento y ubicación.

---

## 4. Registro de Temperaturas Diarias (`registro_temperatura365d_smn.txt`)
- **Fuente**: Servicio Meteorológico Nacional (SMN) https://smn.gob.ar/
- **Fecha de adquisición**: mayo de 2025.
- **Método de adquisición**: Navegación directa en el sitio del SMN y descarga del archivo histórico correspondiente.
- **Descripción**: Temperaturas máximas y mínimas diarias de múltiples estaciones meteorológicas.

---

## Consideraciones Generales
- Todos los datasets fueron almacenados inicialmente en la carpeta `data/raw/`.
- No se aplicaron procesos de transformación ni manipulación en el momento de adquisición, salvo conversión de formato en archivos Excel.
- Los archivos fueron seleccionados manualmente navegando cada portal y descargando únicamente aquellos pertinentes al objetivo del proyecto.

---
