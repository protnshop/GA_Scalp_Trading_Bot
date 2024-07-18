
import pandas as pd

def simulate_real_time_trading(best_params, data, live_data_func):
    initial_capital = 100000.0
    position = 0
    cash = initial_capital
    
    for index, row in data.iterrows():
        live_data = live_data_func(index, data)
        strategy = define_strategy(live_data, **best_params)
        signal = strategy['signal'].iloc[-1]
        
        if signal == 1.0 and position == 0:
            position = 1000  # Buy 1000 units
            cash -= position * row['Adj Close']
        elif signal == 0.0 and position != 0:
            cash += position * row['Adj Close']
            position = 0  # Sell all units
        
        portfolio_value = cash + (position * row['Adj Close'])
        print(f"Date: {index}, Portfolio Value: {portfolio_value}")

def live_data_func(current_index, historical_data):
    return historical_data[:current_index]
