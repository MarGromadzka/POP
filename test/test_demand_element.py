import pytest

from src.evolution_model.individual import Individual
from src.evolution_model.demand_element import DemandElement
from src.load_data import load_demands, load_paths
from src.evolution_model.transponders import Transponder100G, Transponder200G, Transponder400G


@pytest.fixture()
def determined_demand_paths():
    work_set = "../data/polska_small/"
    demand_paths = load_paths(work_set)
    return demand_paths[0].paths


@pytest.fixture()
def determined_demand():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    return demands[0]


@pytest.fixture()
def determined_demand_element(determined_demand, determined_demand_paths):
    demand_element = DemandElement(determined_demand, determined_demand_paths)
    return demand_element


@pytest.fixture
def determined_demand_element():
    work_set = "../data/polska_small/"
    demands = load_demands(work_set)
    demand_paths = load_paths(work_set)
    individual = Individual()
    individual.generate_deterministic(demands, demand_paths, Transponder100G())
    demand_element = individual.demand_elements[0]
    return demand_element


def test_proper_size(determined_demand_element):
    determined_demand_element.bitrate_threshold = 1249
    determined_demand_element.generate_deterministic_transponders(Transponder100G())
    transponders_count = determined_demand_element.count_transponders()
    assert transponders_count["100G"] == 13
    determined_demand_element.generate_deterministic_transponders(Transponder200G())
    transponders_count = determined_demand_element.count_transponders()
    assert transponders_count["200G"] == 7
    determined_demand_element.generate_deterministic_transponders(Transponder400G())
    transponders_count = determined_demand_element.count_transponders()
    assert transponders_count["400G"] == 4


def test_random_creation(determined_demand, determined_demand_paths):
    demand_element = DemandElement(determined_demand, determined_demand_paths)
    assert demand_element.calculate_provided_bitrate() > 110




    # demand_element.mutate()