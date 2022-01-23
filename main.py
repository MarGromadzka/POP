from src.load_data import load_nodes, load_links, load_demands, load_paths
from src.evolution_model.individual import Individual

if __name__ == "__main__":
    work_set = "data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual(demands, demand_paths)
    individual.calculate_cost()
    print(individual.calculate_link_coverage())