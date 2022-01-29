from src.evolution_model.individual import Individual
import random


def crossover(parent_one, parent_two, prob):
    offspring_one = Individual()
    offspring_two = Individual()
    parent_one_elements = parent_one.get_demand_elements()
    parent_two_elements = parent_two.get_demand_elements()
    if len(parent_one_elements) != len(parent_two_elements):
        raise Exception("Number of demand elements should be the same for both parents")
    for i in range(len(parent_one_elements)):
        if random.uniform(0, 1) > prob:
            offspring_one.add_demand_element(parent_one.get_demand_element_from_index(i))
            offspring_two.add_demand_element(parent_two.get_demand_element_from_index(i))
        else:
            offspring_one.add_demand_element(parent_two.get_demand_element_from_index(i))
            offspring_two.add_demand_element(parent_one.get_demand_element_from_index(i))
    return offspring_one, offspring_two

        # tu chyba powinno się pojawić deepcopy
