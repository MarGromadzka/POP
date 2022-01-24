from demand_element import DemandElement
from individual import Individual
import random


def crossover(parent_one, parent_two, prob):
    offspring_one = Individual()
    offspring_two = Individual()
    parent_one_gens = parent_one.get_demand_elements()
    parent_two_gens = parent_two.get_demand_elements()
    if len(parent_one_gens) == len(parent_two_gens):
        raise Exception("It should not be possible")
    for i in range(len(parent_one_gens)):
        if random.uniform(0, 1) > prob:
            offspring_one.add_demand_gen(parent_one.get_demand_element_from_index(i))
            offspring_two.add_demand_gen(parent_two.get_demand_element_from_index(i))
        else:
            offspring_one.add_demand_gen(parent_two.get_demand_element_from_index(i))
            offspring_two.add_demand_gen(parent_one.get_demand_element_from_index(i))
    return offspring_one, offspring_one

        # tu chyba powinno się pojawić deepcopy
