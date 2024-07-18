
# GA Scalp Trading Bot

This project is a genetic algorithm-based scalp trading bot. It uses a combination of technical indicators to generate trading signals and optimizes the strategy using a genetic algorithm.

## Project Structure
```
GA_Scalp_Trading_Bot/
├── data/
│   ├── historical_data.csv
│   └── live_data_mock.csv
├── notebooks/
│   ├── data_analysis.ipynb
│   ├── genetic_algorithm.ipynb
│   └── real_time_simulation.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── strategy.py
│   ├── genetic_algorithm.py
│   └── real_time_trading.py
├── tests/
│   ├── test_data_loader.py
│   ├── test_strategy.py
│   ├── test_genetic_algorithm.py
│   └── test_real_time_trading.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
```
git clone https://github.com/yourusername/GA_Scalp_Trading_Bot.git
cd GA_Scalp_Trading_Bot
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Download historical data and save it to the `data/` directory.

## Usage

### Data Analysis
Open the `data_analysis.ipynb` notebook to explore and analyze the historical data.

### Genetic Algorithm
Open the `genetic_algorithm.ipynb` notebook to develop and test the genetic algorithm for optimizing the trading strategy.

### Real-time Simulation
Open the `real_time_simulation.ipynb` notebook to simulate real-time trading using the optimized strategy.

## Testing
Run the tests using `pytest`:
```
pytest tests/
```

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License.
