from src.evolution_model.population_operators import initiate_population, crossover_population
from src.load_data import load_nodes, load_links, load_demands, load_paths


if __name__ == "__main__":
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    population = initiate_population(10, demands, demand_paths)
    population + crossover_population(population)