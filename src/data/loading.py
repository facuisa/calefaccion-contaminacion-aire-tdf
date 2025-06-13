import pandas as pd

def load_pm10(path='../data/raw/pm 10 coyhaique (extended).csv'):
    return pd.read_csv(path, sep=';', encoding='latin1', engine='python')

def load_pm25(path='../data/raw/pm 2.5 coyhaique.csv'):
    return pd.read_csv(path, sep=';')

def load_co(path='../data/raw/CO coyhaique.csv'):
    return pd.read_csv(path, sep=';')

def load_so2(path='../data/raw/SO2 coyahique.csv'):
    return pd.read_csv(path, sep=';')

def load_meteo(path='../data/raw/export (extended).csv'):
    return pd.read_csv(path)

def load_umbrales_pm10(path='../data/raw/umbrales_pm10.csv'):
    return pd.read_csv(path, sep=';')