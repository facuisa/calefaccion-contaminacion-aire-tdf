# src/features/build_features.py

import pandas as pd

def clasificar_riesgo(pm10_value, umbrales_df):
    if pd.isnull(pm10_value):
        return 'Desconocido'
    for _, row in umbrales_df.iterrows():
        if row['pm10_min'] <= pm10_value <= row['pm10_max']:
            return row['riesgo']
    return 'Fuera de rango'

def agregar_riesgo(df_pm10, umbrales_df):
    df_pm10['Riesgo'] = df_pm10['PM10'].apply(lambda x: clasificar_riesgo(x, umbrales_df))
    return df_pm10

def unir_contaminantes(df_pm10, df_pm25, df_co, df_so2):
    # Filtramos solo las columnas necesarias
    df_pm10 = df_pm10[['PM10', 'Riesgo']].copy()
    df_pm25 = df_pm25[['PM2.5']].copy()
    df_co = df_co[['CO']].copy()
    df_so2 = df_so2[['SO2']].copy()

    # Unimos todos los contaminantes por índice de fecha-hora
    df_total = df_pm10.join([df_pm25, df_co, df_so2], how='inner')
    return df_total

def agregar_meteorologia(df_total, df_meteo):
    # Crear columna de fecha en ambos dataframes
    df_total['fecha'] = df_total.index.date
    df_meteo['fecha'] = df_meteo.index.date

    # Merge por fecha
    df_total = df_total.merge(df_meteo, on='fecha', how='left')

    # Eliminar columna auxiliar
    df_total = df_total.drop(columns=['fecha'])

    return df_total