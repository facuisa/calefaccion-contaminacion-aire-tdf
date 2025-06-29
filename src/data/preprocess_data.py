# src/data/preprocess_data.py

import pandas as pd

def process_pm(df):
    df = df.drop(columns=['Unnamed: 5', 'Registros preliminares', 'Registros no validados'], errors='ignore')
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA (YYMMDD)'].astype(str) + df['HORA (HHMM)'].astype(str).str.zfill(4), format='%y%m%d%H%M')
    df = df.set_index('FECHA_HORA')
    nulls = df[df['Registros validados'].isnull()]
    nulos_por_dia = nulls.groupby(nulls.index.date).size()
    dias_completos_nulos = nulos_por_dia[nulos_por_dia == 24].index.tolist()
    df = df[[date not in dias_completos_nulos for date in df.index.date]]
    df['Registros validados'] = df['Registros validados'].interpolate(method='time')
    return df

def clean_pm10(df):
    df = process_pm(df)
    df = df.rename(columns={'Registros validados': 'PM10'})
    return df

def clean_pm25(df):
    df = process_pm(df)
    df = df.rename(columns={'Registros validados': 'PM2.5'})
    return df

def clean_co(df):
    df = df.drop(columns=['Registros preliminares', 'Registros no validados', 'Unnamed: 5'], errors='ignore')
    df['Registros validados'] = df['Registros validados'].str.replace(',', '.').astype(float)
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA (YYMMDD)'].astype(str) + df['HORA (HHMM)'].astype(str).str.zfill(4), format='%y%m%d%H%M')
    df = df.set_index('FECHA_HORA')
    nulls = df[df['Registros validados'].isnull()]
    nulos_por_dia = nulls.groupby(nulls.index.date).size()
    dias_completos_nulos = nulos_por_dia[nulos_por_dia == 24].index.tolist()
    df = df[[date not in dias_completos_nulos for date in df.index.date]]
    df['Registros validados'] = df['Registros validados'].interpolate(method='time')
    return df.rename(columns={'Registros validados': 'CO'})

def clean_so2(df):
    df = df.drop(columns=['Registros preliminares', 'Registros no validados', 'Unnamed: 5'], errors='ignore')
    df['Registros validados'] = pd.to_numeric(df['Registros validados'], errors='coerce')
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA (YYMMDD)'].astype(str) + df['HORA (HHMM)'].astype(str).str.zfill(4), format='%y%m%d%H%M')
    df = df.set_index('FECHA_HORA')
    nulls = df[df['Registros validados'].isnull()]
    nulos_por_dia = nulls.groupby(nulls.index.date).size()
    dias_completos_nulos = nulos_por_dia[nulos_por_dia == 24].index.tolist()
    df = df[[date not in dias_completos_nulos for date in df.index.date]]
    df['Registros validados'] = df['Registros validados'].interpolate(method='time')
    return df.rename(columns={'Registros validados': 'SO2'})

def clean_meteo(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df[['date', 'tmin', 'tavg', 'tmax', 'prcp', 'wspd', 'pres']]
    df = df.set_index('date')
    return df.interpolate(method='time')