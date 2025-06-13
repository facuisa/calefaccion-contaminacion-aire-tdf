import pandas as pd

def procesar_contaminante(df, nombre_col, decimal_coma=False):
    df = df.drop(columns=['Registros preliminares', 'Registros no validados', 'Unnamed: 5'], errors='ignore')
    if decimal_coma:
        df['Registros validados'] = df['Registros validados'].str.replace(',', '.').astype(float)
    else:
        df['Registros validados'] = pd.to_numeric(df['Registros validados'], errors='coerce')
    df['FECHA_HORA'] = pd.to_datetime(
        df['FECHA (YYMMDD)'].astype(str) + df['HORA (HHMM)'].astype(str).str.zfill(4),
        format='%y%m%d%H%M'
    )
    df = df.set_index('FECHA_HORA')
    nulls = df[df['Registros validados'].isnull()]
    nulos_por_dia = nulls.groupby(nulls.index.date).size()
    dias_completos = nulos_por_dia[nulos_por_dia == 24].index.tolist()
    mask = [date not in dias_completos for date in df.index.date]
    df = df[mask]
    df['Registros validados'] = df['Registros validados'].interpolate(method='time')
    return df.rename(columns={'Registros validados': nombre_col})[[nombre_col]]

def procesar_meteorologia(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df[['date', 'tmin', 'tavg', 'tmax', 'prcp', 'wspd', 'pres']]
    df = df.set_index('date')
    df = df.interpolate(method='time')
    return df

def clasificar_riesgo(pm10, umbrales_df):
    """Clasifica el nivel de riesgo en base al valor de PM10 y los umbrales proporcionados."""
    if pd.isnull(pm10):
        return 'Desconocido'
    for _, row in umbrales_df.iterrows():
        if row['pm10_min'] <= pm10 <= row['pm10_max']:
            return row['riesgo']
    return 'Fuera de rango'

def clasificar_riesgo(pm10, umbrales_df):
    """Clasifica el nivel de riesgo en base al valor de PM10 y los umbrales proporcionados."""
    if pd.isnull(pm10):
        return 'Desconocido'
    for _, row in umbrales_df.iterrows():
        if row['pm10_min'] <= pm10 <= row['pm10_max']:
            return row['riesgo']
    return 'Fuera de rango'

def unir_datasets(df_pm10, df_pm25, df_co, df_so2, df_meteo, df_umbrales):
    """Une todos los datasets preprocesados y clasifica el riesgo."""

    df_pm10 = df_pm10.copy()
    df_pm10['Riesgo'] = df_pm10['PM10'].apply(lambda x: clasificar_riesgo(x, df_umbrales))

    # Filtramos solo las columnas necesarias
    df_pm10 = df_pm10[['PM10', 'Riesgo']]
    df_pm25 = df_pm25[['PM2.5']]
    df_co = df_co[['CO']]
    df_so2 = df_so2[['SO2']]

    # Unión de contaminantes
    df_total = df_pm10.join([df_pm25, df_co, df_so2], how='inner')

    # Unión con datos meteorológicos (por fecha)
    df_total['fecha'] = df_total.index.date
    df_meteo['fecha'] = df_meteo.index.date
    df_total = df_total.merge(df_meteo, on='fecha', how='left')
    df_total = df_total.drop(columns=['fecha'])

    return df_total