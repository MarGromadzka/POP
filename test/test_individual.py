from src.evolution_model.individual import Individual
from src.load_data import load_demands, load_paths
from src.evolution_model.transponders import Transponder100G


def test_creation():
    # test for hardcoded example
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual(demands, demand_paths)
    assert len(individual.demand_elements) == 3
    assert individual.demand_elements[0].bitrate_threshold == 110
    # założenie, że są same transpondery 100 G
    assert len(individual.demand_elements[0].path_elements) == 2
    assert individual.calculate_cost() == 15
    links_dict = individual.calculate_link_coverage()
    assert links_dict['Link_3_6'] == 2
    assert links_dict['Link_3_11'] == 1
    assert links_dict['Link_6_11'] == 2

def test_mutation():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual(demands, demand_paths)
    demand_element = individual.demand_elements[0]