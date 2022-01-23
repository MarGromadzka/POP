from src.evolution_model.individual import Individual
from src.load_data import load_demands, load_paths
from src.evolution_model.transponders import Transponder100G


def test_demand_element():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual(demands, demand_paths)
    demand_element = individual.demand_elements[0]
    transponders_count = demand_element.count_transponders()
    assert transponders_count["100G"] == 2
    demand_element.mutate(0.0)
    transponders_count = demand_element.count_transponders()
    print(transponders_count)

    # demand_element.mutate()