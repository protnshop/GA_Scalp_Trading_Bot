
import pandas as pd
import numpy as np

def define_strategy(data, short_window=40, long_window=100, rsi_period=14, bb_window=20):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    # Moving Average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    # RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period, min_periods=1).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period, min_periods=1).mean()
    RS = gain / loss
    signals['RSI'] = 100 - (100 / (1 + RS))
    
    # Bollinger Bands
    signals['BB_Mid'] = data['Close'].rolling(window=bb_window, min_periods=1).mean()
    signals['BB_Upper'] = signals['BB_Mid'] + 2 * data['Close'].rolling(window=bb_window, min_periods=1).std()
    signals['BB_Lower'] = signals['BB_Mid'] - 2 * data['Close'].rolling(window=bb_window, min_periods=1).std()
    
    # Generate signals
    signals['signal'] = np.where(
        (signals['short_mavg'] > signals['long_mavg']) & 
        (signals['RSI'] < 70) & 
        (data['Close'] < signals['BB_Upper']), 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals
