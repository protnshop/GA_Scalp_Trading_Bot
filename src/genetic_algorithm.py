
import random
import pandas as pd

def fitness_function(strategy, data):
    initial_capital = float(100000.0)
    positions = pd.DataFrame(index=data.index).fillna(0.0)
    portfolio = pd.DataFrame(index=data.index).fillna(0.0)
    positions['Asset'] = strategy['signal'] * 1000
    portfolio['positions'] = positions.multiply(data['Adj Close'], axis=0)
    pos_diff = positions.diff()
    portfolio['cash'] = initial_capital - (pos_diff.multiply(data['Adj Close'], axis=0)).cumsum()
    portfolio['total'] = portfolio['positions'] + portfolio['cash']
    returns = portfolio['total'].pct_change()
    sharpe_ratio = returns.mean() / returns.std()
    return sharpe_ratio

def selection(population, data):
    fitness_scores = [(strategy, fitness_function(strategy, data)) for strategy in population]
    fitness_scores = sorted(fitness_scores, key=lambda x: x[1], reverse=True)
    return [x[0] for x in fitness_scores[:len(population) // 2]]

def crossover(parent1, parent2):
    child = {}
    for key in parent1.keys():
        if random.random() > 0.5:
            child[key] = parent1[key]
        else:
            child[key] = parent2[key]
    return child

def mutation(strategy):
    if random.random() < 0.1:  # 10% chance of mutation
        param = random.choice(['short_window', 'long_window', 'rsi_period', 'bb_window'])
        if param in ['short_window', 'long_window', 'bb_window']:
            strategy[param] = max(1, int(strategy[param] * (1 + random.uniform(-0.2, 0.2))))
        elif param == 'rsi_period':
            strategy[param] = max(1, int(strategy[param] * (1 + random.uniform(-0.2, 0.2))))
    return strategy

def run_genetic_algorithm(data, num_generations=10, population_size=20):
    # Initialize population with random strategies
    population = [{'short_window': random.randint(10, 50), 'long_window': random.randint(50, 200), 'rsi_period': random.randint(10, 30), 'bb_window': random.randint(10, 50)} for _ in range(population_size)]
    
    for generation in range(num_generations):
        # Evaluate fitness
        strategies = [define_strategy(data, **params) for params in population]
        population = selection(strategies, data)
        
        # Crossover
        new_population = []
        for i in range(len(population) // 2):
            parent1 = population[i]
            parent2 = population[-i-1]
            child_params = crossover(parent1, parent2)
            new_population.append(child_params)
        
        # Mutation
        new_population = [mutation(params) for params in new_population]
        
        # Create new strategies for the next generation
        population = new_population
        
        # Print the best fitness score
        best_strategy = define_strategy(data, **population[0])
        best_fitness = fitness_function(best_strategy, data)
        print(f'Generation {generation+1}: Best fitness = {best_fitness}')
    
    # Return the best strategy
    return population[0]
