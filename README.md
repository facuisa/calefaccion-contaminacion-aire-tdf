# PREDICCIÓN DE DÍAS CON RIESGO DE CONTAMINACIÓN POR CALEFACCIÓN DOMICILIARIA

## **Objetivo:**
Este proyecto tiene como objetivo desarrollar un modelo de clasificación supervisada que permita predecir qué días presentan riesgo elevado de contaminación del aire en zonas urbanas de Tierra del Fuego, especialmente en las ciudades de Río Grande y Ushuaia, como consecuencia del uso intensivo de calefacción domiciliaria a gas o leña. Esta situación puede agravar problemas respiratorios, particularmente en niños y adultos mayores. Para ello, se utilizarán variables climáticas, de consumo energético y de calidad del aire como insumos del modelo.

## **Contexto del Problema:**
Tierra del Fuego es una provincia con un clima riguroso, donde la calefacción es esencial para la calidad de vida. Sin embargo, el uso masivo de sistemas de calefacción a gas, leña o combustibles fósiles, genera emisiones que impactan negativamente en la calidad del aire, agravando enfermedades respiratorias y afectando el bienestar de la población, especialmente en zonas urbanas con alta densidad habitacional como Ushuaia y Río Grande.

## **Interrogantes de estudio:**
¿Qué nivel de precisión puede alcanzar un modelo supervisado al predecir días con riesgo elevado de contaminación atmosférica por calefacción domiciliaria?

¿Cuáles son las variables climáticas, energéticas o ambientales más relevantes en la predicción de estos episodios?

¿Es posible aplicar el modelo como herramienta de apoyo para la toma de decisiones en políticas públicas, alertas tempranas o acciones de concientización ambiental?

## **Relevancia:**
Anticipar días con condiciones propicias para la acumulación de contaminantes permitiría tomar decisiones informadas en materia de salud pública y medioambiente. Por ejemplo, implementar alertas tempranas, restringir quemas domiciliarias o promover el uso de sistemas más eficientes durante esos días.

## **Alcance:**
Aunque el modelo se entrena con datos de **Coyhaique**, su objetivo es sentar las bases para un sistema predictivo aplicable a Tierra del Fuego. La metodología puede adaptarse a datos locales en el futuro e integrarse a plataformas de monitoreo ambiental o decisiones gubernamentales.

## **Machine Learning for Predicting Air Pollution Risk Days from Domestic Heating**
This project aims to develop a supervised classification model to predict high-risk air pollution days in Tierra del Fuego due to domestic heating during cold months. Using variables such as minimum daily temperature, wind speed, atmospheric pressure, and energy consumption, the model learns to identify conditions favorable for pollutant accumulation. It also includes air quality measures such as PM2.5, PM10, and NO₂. Early detection of these days may inform public policies, awareness campaigns, and help protect vulnerable populations.

# Estructura del Proyecto

```text
calefaccion-contaminacion-aire-tdf/
├── data/
│   ├── raw/                  # Datos originales sin procesar
│   ├── processed/            # Datos listos para entrenar
│   └── interim/              # Datos intermedios
│
├── docs/                     # Documentación del proyecto
│   └── dataset_description.md
│
├── models/                   # Modelos entrenados y serializados
│
├── notebooks/                # Jupyter notebooks para análisis exploratorio, entrenamiento y pruebas
│   └── Modelo de Clasificación de Días de riesgo por contaminacion.ipynb
│
├── references/               # Artículos, papers, papers técnicos o benchmarks
│
├── reports/
│   ├── figures/              # Gráficos generados automáticamente
│   └── evaluation.md         # Reportes de evaluación del modelo
│
├── src/                      # Código fuente del proyecto
│   ├── data/                 # Scripts para carga, limpieza y transformación
│   ├── features/             # Scripts de ingeniería de características
│   ├── models/               # Scripts de entrenamiento, evaluación y predicción
│   └── visualization/        # Funciones de gráficos y visualización
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
