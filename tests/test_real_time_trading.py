
import unittest
from src.real_time_trading import simulate_real_time_trading, live_data_func
from src.data_loader import load_historical_data

class TestRealTimeTrading(unittest.TestCase):
    def setUp(self):
        self.data = load_historical_data('data/historical_data.csv')
        self.best_params = {'short_window': 40, 'long_window': 100, 'rsi_period': 14, 'bb_window': 20}
    
    def test_simulate_real_time_trading(self):
        simulate_real_time_trading(self.best_params, self.data, live_data_func)

if __name__ == '__main__':
    unittest.main()
