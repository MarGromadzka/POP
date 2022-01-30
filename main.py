import random
import statistics
from src.evolution_model.population_operators import initiate_population, crossover_population, succession, \
    mutate_population
from src.load_data import load_demands, load_paths
import csv
import matplotlib.pyplot as plt


def evolution_alg(pop_size, cross_size, su_size, gen, mut_prob, cross_prob=0.5):
    population = initiate_population(demands, demand_paths, pop_size)
    print(f"Population size: {pop_size} Number of generations: {gen} Mutation probability: {mut_prob} Crossover probability: {cross_prob}")
    min_cost = []
    mean_cost = []
    link_cov = []
    for _ in range(gen):
        new_population = crossover_population(population, cross_size, cross_prob)
        new_population = mutate_population(new_population, mut_prob)
        population = succession(population + new_population, su_size)
        min_cost.append(min([individual.calculate_cost() for individual in population]))
        mean_cost.append(statistics.mean([individual.calculate_cost() for individual in population]))
        link_cov.append(min([max(individual.calculate_link_coverage().values()) for individual in population]))
    return min_cost, mean_cost, link_cov


def make_plot(list_1, list_2, plot_title, file_title):
    plt.plot(list_2, list_1)
    plt.title(f"{plot_title}")
    plt.savefig(f"{file_title}")
    plt.clf()


def write_to_csv(table, title):
    with open(title, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(table)


def experiments():
    population_size = 100
    crossover_size = 100  # must be even
    succession_size = 100
    generations = 100
    mutation_probability = 0.3
    general_min = []
    general_mean = []
    general_lincov = []
    y1 = [x for x in range(1, 101, 1)]
    y2 = [x for x in range(10, 101, 10)]
    for size in range(10, 101, 10):
        min_c, mean_c, link_cov = evolution_alg(size, size, size, generations, mutation_probability)
        general_min.append(min_c[-1])
        general_mean.append((mean_c[-1]))
        general_lincov.append(link_cov[-1])
        write_to_csv(min_c, f"results\\min_s{size}_g100_m30.csv")
        write_to_csv(mean_c, f"results\\mean_s{size}_g100_m30.csv")
        write_to_csv(link_cov, f"results\\lc_s{size}_g100_m30.csv")
        make_plot(min_c, y1, "Minimalny koszt w kolejnych pokoleniach", f"results\\min_s{size}_g100_m30")
        make_plot(mean_c, y1, "Średnia kosztu w kolejnych pokoleniach", f"results\\mean_s{size}_g100_m30")
        make_plot(link_cov, y1, "Zajętość połączeń w kolejnych pokoleniach",  f"results\\lc_s{size}_g100_m30")
    write_to_csv(general_min, f"results\\gen_min_size_g100_m30.csv")
    write_to_csv(general_mean, f"results\\gen_mean_size_g100_m30.csv")
    write_to_csv(general_lincov, f"results\\gen_lc_size_g100_m30.csv")
    make_plot(general_min, y2, "Minimalny koszt dla różnych wielkości populacji", f"results\\gen_min_size_g100_m30")
    make_plot(general_mean, y2, "Średni koszt dla różnych wielkości populacji", f"results\\gen_mean_size_g100_m30")
    make_plot(general_lincov, y2, "Zajętość połączeń najlepszego osobnika z populacji dla różnych wielkości populacji", f"results\\gen_lc_size_g100_m30")

    general_min = []
    general_mean = []
    general_lincov = []
    for gen in range(10, 101, 10):
        min_c, mean_c, link_cov = evolution_alg(population_size, crossover_size, succession_size, gen,
                                                mutation_probability)
        general_min.append(min_c[-1])
        general_mean.append((mean_c[-1]))
        general_lincov.append(link_cov[-1])
        write_to_csv(min_c, f"results\\min_s100_g{gen}_m30.csv")
        write_to_csv(mean_c, f"results\\mean_s100_g{gen}_m30.csv")
        write_to_csv(link_cov, f"results\\lc_s100_g{gen}_m30.csv")
        make_plot(min_c, [x for x in range(1, len(min_c)+1, 1)], "Minimalny koszt w kolejnych pokoleniach", f"results\\min_s100_g{gen}_m30")
        make_plot(mean_c, [x for x in range(1, len(min_c)+1, 1)], "Średnia kosztu w kolejnych pokoleniach", f"results\\mean_s100_g{gen}_m30")
        make_plot(link_cov, [x for x in range(1, len(min_c)+1, 1)], "Zajętość połączeń w kolejnych pokoleniach", f"results\\lc_s100_g{gen}_m30")
    write_to_csv(general_min, f"results\\gen_min_size100_gen_m30.csv")
    write_to_csv(general_mean, f"results\\gen_mean_size100_gen_m30.csv")
    write_to_csv(general_lincov, f"results\\gen_lc_size100_gen_m30.csv")
    make_plot(general_min, y2, "Minimalny koszt dla różnej ilości pokoleń", f"results\\gen_min_size100_gen_m30")
    make_plot(general_mean, y2, "Średni koszt dla różnej ilości pokoleń", f"results\\gen_mean_size100_gen_m30")
    make_plot(general_lincov, y2, "Zajętość połączeń najlepszego osobnika z populacji dla różnej ilości pokoleń",
              f"results\\gen_lc_size100_gen_m30")

    general_min = []
    general_mean = []
    general_lincov = []
    for mut in range(10, 110, 10):
        min_c, mean_c, link_cov = evolution_alg(population_size, crossover_size, succession_size, generations,
                                                mut / 100)
        general_min.append(min_c[-1])
        general_mean.append((mean_c[-1]))
        general_lincov.append(link_cov[-1])
        write_to_csv(min_c, f"results\\min_s100_g100_m{mut}.csv")
        write_to_csv(mean_c, f"results\\mean_s100_g100_m{mut}.csv")
        write_to_csv(link_cov, f"results\\lc_s100_g100_m{mut}.csv")
        make_plot(min_c, y1, "Minimalny koszt w kolejnych pokoleniach", f"results\\min_s100_g100_m{mut}")
        make_plot(mean_c, y1, "Średnia kosztu w kolejnych pokoleniach", f"results\\mean_s100_g100_m{mut}")
        make_plot(link_cov, y1, "Zajętość połączeń w kolejnych pokoleniach", f"results\\lc_s100_g100_m{mut}")
    write_to_csv(general_min, f"results\\gen_min_size_gen100_mut.csv")
    write_to_csv(general_mean, f"results\\gen_mean_size_gen100_mut.csv")
    write_to_csv(general_lincov, f"results\\gen_lc_size_gen100_mut.csv")
    make_plot(general_min, y2, "Minimalny koszt dla różnego prawdopodbieństwa mutacji", f"results\\gen_min_size_gen100_mut")
    make_plot(general_mean, y2, "Średni koszt dla różnego prawdopodbieństwa mutacji", f"results\\gen_mean_size_gen100_mut")
    make_plot(general_lincov, y2, "Zajętość połączeń najlepszego osobnika z populacji dla różnego prawdopodbieństwa mutacji",
              f"results\\gen_lc_size_gen100_mut")

    general_min = []
    general_mean = []
    general_lincov = []
    for cross in range(10, 110, 10):
        min_c, mean_c, link_cov = evolution_alg(population_size, crossover_size, succession_size, generations,
                                                mutation_probability, cross / 100)
        general_min.append(min_c[-1])
        general_mean.append((mean_c[-1]))
        general_lincov.append(link_cov[-1])
        write_to_csv(min_c, f"results\\min_s100_g100_m30_c{cross}.csv")
        write_to_csv(mean_c, f"results\\mean_s100_g100_m30_c{cross}.csv")
        write_to_csv(link_cov, f"results\\lc_s100_g100_m30_c{cross}.csv")
        make_plot(min_c, y1, "Minimalny koszt w kolejnych pokoleniach",  f"results\\min_s100_g100_m30_c{cross}")
        make_plot(mean_c, y1, "Średnia kosztu w kolejnych pokoleniach", f"results\\mean_s100_g100_m30_c{cross}")
        make_plot(link_cov, y1, "Zajętość połączeń w kolejnych pokoleniach", f"results\\lc_s100_g100_m30_c{cross}")
    write_to_csv(general_min, f"results\\gen_min_size_gen100_m30_cross.csv")
    write_to_csv(general_mean, f"results\\gen_mean_size_gen100_m30_cross.csv")
    write_to_csv(general_lincov, f"results\\gen_lc_size_gen100_m30_cross.csv")
    make_plot(general_min, y2, "Minimalny koszt dla różnego prawdopodbieństwa krzyżowania",
              f"results\\gen_min_size_gen100_m30_cross")
    make_plot(general_mean, y2, "Średni koszt dla różnego prawdopodbieństwa krzyżowania",
              f"results\\gen_mean_size_gen100_m30_cross")
    make_plot(general_lincov, y2,
              "Zajętość połączeń najlepszego osobnika z populacji dla różnego prawdopodbieństwa krzyżowania",
              f"results\\gen_lc_size_gen100_m30_cross")


if __name__ == "__main__":
    random.seed(123)
    work_set = "data/polska/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    experiments()
