
import unittest
import pandas as pd
from src.strategy import define_strategy

class TestStrategy(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('data/historical_data.csv', index_col='Date', parse_dates=True)
    
    def test_define_strategy(self):
        strategy = define_strategy(self.data)
        self.assertIn('signal', strategy.columns)
        self.assertIn('positions', strategy.columns)

if __name__ == '__main__':
    unittest.main()
