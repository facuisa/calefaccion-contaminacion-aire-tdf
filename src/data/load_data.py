# src/data/load_data.py

import pandas as pd

def load_pm10(path):
    return pd.read_csv(path, sep=';', encoding='latin1', engine='python')

def load_pm25(path):
    return pd.read_csv(path, sep=';')

def load_co(path):
    return pd.read_csv(path, sep=';')

def load_so2(path):
    return pd.read_csv(path, sep=';')

def load_meteo(path):
    return pd.read_csv(path)

def load_umbrales_pm10(path):
    return pd.read_csv(path, sep=';')