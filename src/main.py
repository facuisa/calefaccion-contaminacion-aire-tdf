# src/main.py

import os
import pandas as pd

# ==== 1. CARGA DE DATOS RAW ====
from src.data.load_data import (
    load_pm10, load_pm25, load_co, load_so2,
    load_meteo, load_umbrales_pm10
)

# ==== 2. PREPROCESAMIENTO ====
from src.data.preprocess_data import (
    clean_pm10, clean_pm25, clean_co,
    clean_so2, clean_meteo
)

# ==== 3. INGENIERÍA DE FEATURES ====
from src.features.build_features import (
    agregar_riesgo, unir_contaminantes, agregar_meteorologia
)

# ==== 4. VISUALIZACIÓN ====
from src.visualization.visualize import (
    plot_histograms, plot_boxplots_vs_riesgo, plot_correlation_matrix
)

# ==== 5. MODELADO ====
from src.models.train_model import (
    preparar_datos, escalar_datos,
    entrenar_gridsearch, evaluar_modelo,
    comparar_modelos
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def main():

    print("\n🚀 Iniciando pipeline completo...\n")

    # === RUTAS ===
    data_path = 'data/raw/'
    umbrales_path = os.path.join(data_path, 'umbrales_pm10.csv')

    # === CARGA ===
    df_pm10 = load_pm10(os.path.join(data_path, 'pm 10 coyhaique (extended).csv'))
    df_pm25 = load_pm25(os.path.join(data_path, 'pm 2.5 coyhaique.csv'))
    df_co = load_co(os.path.join(data_path, 'CO coyhaique.csv'))
    df_so2 = load_so2(os.path.join(data_path, 'SO2 coyahique.csv'))
    df_meteo = load_meteo(os.path.join(data_path, 'export (extended).csv'))
    umbrales_df = load_umbrales_pm10(umbrales_path)

    print("✅ Archivos cargados")

    # === LIMPIEZA ===
    df_pm10 = clean_pm10(df_pm10)
    df_pm25 = clean_pm25(df_pm25)
    df_co = clean_co(df_co)
    df_so2 = clean_so2(df_so2)
    df_meteo = clean_meteo(df_meteo)

    print("🧹 Datos limpiados")

    # === FEATURES ===
    df_pm10 = agregar_riesgo(df_pm10, umbrales_df)
    df_total = unir_contaminantes(df_pm10, df_pm25, df_co, df_so2)
    df_total = agregar_meteorologia(df_total, df_meteo)

    print(f"🧩 Dataset final generado: {df_total.shape[0]} registros, {df_total.shape[1]} columnas")

    # === VISUALIZACIONES (opcional) ===
    print("\n📊 Generando visualizaciones...")
    plot_histograms(df_total)
    plot_boxplots_vs_riesgo(df_total, ['PM2.5', 'CO', 'tavg', 'tmin', 'tmax', 'wspd'])
    plot_correlation_matrix(df_total)

    # === MODELADO ===
    print("\n🤖 Preparando datos para modelado...")
    X, y, le = preparar_datos(df_total)
    X_train, X_test, y_train, y_test = escalar_datos(X, y)

    # Árbol de Decisión
    print("\n🌳 Entrenando Árbol de Decisión...")
    param_dt = {
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'criterion': ['gini', 'entropy']
    }
    modelo_dt, _, _ = entrenar_gridsearch(
        DecisionTreeClassifier(random_state=42), param_dt, X_train, y_train
    )
    report_dt, _ = evaluar_modelo(modelo_dt, X_test, y_test, le, 'Árbol de Decisión')

    # Random Forest
    print("\n🌲 Entrenando Random Forest...")
    param_rf = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'criterion': ['gini', 'entropy']
    }
    modelo_rf, _, _ = entrenar_gridsearch(
        RandomForestClassifier(random_state=42), param_rf, X_train, y_train
    )
    report_rf, _ = evaluar_modelo(modelo_rf, X_test, y_test, le, 'Random Forest')

    # Comparación
    print("\n📈 Comparación de Modelos:")
    comparar_modelos(report_dt, report_rf)


if __name__ == "__main__":
    main()