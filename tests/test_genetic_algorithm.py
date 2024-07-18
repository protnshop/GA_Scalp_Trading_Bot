
import unittest
from src.genetic_algorithm import run_genetic_algorithm
from src.data_loader import load_historical_data

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.data = load_historical_data('data/historical_data.csv')
    
    def test_run_genetic_algorithm(self):
        best_params = run_genetic_algorithm(self.data, num_generations=2, population_size=5)
        self.assertIsInstance(best_params, dict)
        self.assertIn('short_window', best_params)
        self.assertIn('long_window', best_params)

if __name__ == '__main__':
    unittest.main()
