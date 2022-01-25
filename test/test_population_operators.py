from src.evolution_model.population_operators import initiate_population, crossover_population
from src.load_data import load_demands, load_paths


def test_initiate_population():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    population = initiate_population(demands, demand_paths, 10)
    assert len(population) == 10


def test_crossover_population():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    population = initiate_population(demands, demand_paths, 10)
    offspring = crossover_population(population, 5)
    assert len(population + offspring) == 20
