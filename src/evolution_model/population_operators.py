from src.evolution_model.individual import Individual
from src.evolution_model.crossover import crossover
import random


def initiate_population(demands, demand_paths, size):
    population = []
    for _ in range(size):
        individual = Individual()
        individual.generate_random(demands, demand_paths)
        population.append(individual)
    return population


def crossover_population(population, size):
    offspring = []
    for _ in range(size):
        [parent_one, parent_two] = random.sample(population, 2)
        offspring_one, offspring_two = crossover(parent_one, parent_two, 0.5)
        offspring.append(offspring_one)
        offspring.append(offspring_two)
    return offspring
