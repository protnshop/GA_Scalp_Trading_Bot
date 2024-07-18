 
import pandas as pd

def load_historical_data(filepath):
    data = pd.read_csv(filepath, index_col='Date', parse_dates=True)
    return data

def load_live_data(filepath):
    data = pd.read_csv(filepath, index_col='Date', parse_dates=True)
    return data
