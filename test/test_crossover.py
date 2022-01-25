import pytest

from src.evolution_model.crossover import crossover
from src.evolution_model.individual import Individual
from src.load_data import load_demands, load_paths
from src.evolution_model.transponders import Transponder100G, Transponder200G


@pytest.fixture
def determined_individual_100g():
    # test for hardcoded example
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual()
    individual.generate_deterministic(demands, demand_paths, Transponder100G())
    return individual


@pytest.fixture()
def determined_individual_200g():
    # test for hardcoded example
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual()
    individual.generate_deterministic(demands, demand_paths, Transponder200G())
    return individual


def test_crossover(determined_individual_100g, determined_individual_200g):
    offspring_one, offspring_two = crossover(determined_individual_100g, determined_individual_200g, 1.0)
    transponders_one = offspring_one.get_demand_element_from_index(0).count_transponders()
    assert transponders_one['200G'] == 1
    transponders_two = offspring_two.get_demand_element_from_index(0).count_transponders()
    assert transponders_two['100G'] == 2
