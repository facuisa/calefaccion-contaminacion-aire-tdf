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