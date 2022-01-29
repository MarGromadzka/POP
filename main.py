import random

from src.evolution_model.population_operators import initiate_population, crossover_population, succession, \
    mutate_population
from src.load_data import load_demands, load_paths


if __name__ == "__main__":
    random.seed(2137)
    work_set = "data/polska_small/"
    work_set = "data/polska/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    population_size = 100
    crossover_size = 100  # must be even
    succession_size = 100
    generations = 100
    mutation_probability = 0.0
    population = initiate_population(demands, demand_paths, population_size)
    print([individual.calculate_cost() for individual in population])
    for _ in range(generations):
        new_population = crossover_population(population, crossover_size)
        # new_population = mutate_population(new_population, mutation_probability)
        population = succession(population + new_population, succession_size)
        print([individual.calculate_cost() for individual in population])
    print(min([max(individual.calculate_link_coverage().values()) for individual in population]))
