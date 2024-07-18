
import unittest
from src.data_loader import load_historical_data, load_live_data

class TestDataLoader(unittest.TestCase):
    def test_load_historical_data(self):
        data = load_historical_data('data/historical_data.csv')
        self.assertFalse(data.empty)
    
    def test_load_live_data(self):
        data = load_live_data('data/live_data_mock.csv')
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
