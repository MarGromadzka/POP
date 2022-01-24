import pytest

from src.evolution_model.individual import Individual
from src.load_data import load_demands, load_paths
from src.evolution_model.transponders import Transponder100G


@pytest.fixture
def determined_individual():
    # test for hardcoded example
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual()
    individual.generate_deterministic(demands, demand_paths, Transponder100G())
    return individual


def test_elements_number(determined_individual):
    assert len(determined_individual.demand_elements) == 3
    assert determined_individual.demand_elements[0].bitrate_threshold == 110
    # założenie, że są same transpondery 100 G
    assert len(determined_individual.demand_elements[0].path_elements) == 2


def test_calculate_cost(determined_individual):
    assert determined_individual.calculate_cost() == 15


def test_calculate_link_coverage(determined_individual):
    links_dict = determined_individual.calculate_link_coverage()
    assert links_dict['Link_3_6'] == 2
    assert links_dict['Link_3_11'] == 1
    assert links_dict['Link_6_11'] == 2


def test_random_creation():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual()
    individual.generate_random(demands, demand_paths)
    for demand_element in individual.get_demand_elements():
        assert demand_element.calculate_provided_bitrate() >= demand_element.bitrate_threshold
