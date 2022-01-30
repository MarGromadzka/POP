import random
import statistics
from src.evolution_model.population_operators import initiate_population, crossover_population, succession, \
    mutate_population
from src.load_data import load_demands, load_paths
import csv


def evolution_alg(pop_size, cross_size, su_size, gen, mut_prob):
    population = initiate_population(demands, demand_paths, pop_size)
    print(f"Population size: {pop_size} Number of generations: {gen} Mutation probability: {mut_prob}")
    min_cost = []
    mean_cost = []
    link_cov = []
    for _ in range(gen):
        new_population = crossover_population(population, cross_size)
        new_population = mutate_population(new_population, mut_prob)
        population = succession(population + new_population, su_size)
        min_cost.append(min([individual.calculate_cost() for individual in population]))
        mean_cost.append(statistics.mean([individual.calculate_cost() for individual in population]))
        link_cov.append(min([max(individual.calculate_link_coverage().values()) for individual in population]))
    return min_cost, mean_cost, link_cov


def write_to_csv(table, title):
    with open(title, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(table)


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
    mutation_probability = 0.3
    general_min = []
    general_mean = []
    general_lincov = []
    for size in range(10, 100, 10):
        min_c, mean_c, link_cov = evolution_alg(size, size, size, generations, mutation_probability)
        general_min.append(min_c[-1])
        general_mean.append((mean_c[-1]))
        general_lincov.append(link_cov[-1])
        write_to_csv(min_c, f"results\\min_s{size}_g100_m30.csv")
        write_to_csv(mean_c, f"results\\mean_s{size}_g100_m30.csv")
        write_to_csv(link_cov, f"results\\lc_s{size}_g100_m30.csv")
    write_to_csv(general_min, f"results\\gen_min_size_g100_m30.csv")
    write_to_csv(general_mean, f"results\\gen_mean_size_g100_m30.csv")
    write_to_csv(general_lincov, f"results\\gen_lc_size_g100_m30.csv")



    print("")

