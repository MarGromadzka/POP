from copy import deepcopy

from src.evolution_model.demand_element import DemandElement


class Individual:
    def __init__(self):
        self.demand_elements = []

    def generate_random(self, demands, demand_paths):
        for demand in demands:
            paths = list(filter(lambda x: x.demand_id == demand.demand_id, demand_paths))
            self.demand_elements.append(DemandElement(demand, paths[0].paths))

    def generate_deterministic(self, demands, demand_paths, transponder):
        # for test purposes
        for demand in demands:
            paths = list(filter(lambda x: x.demand_id == demand.demand_id, demand_paths))
            demand_element = DemandElement(demand, paths[0].paths)
            demand_element.generate_deterministic_transponders(transponder)
            self.demand_elements.append(demand_element)

    def calculate_cost(self):
        cost = 0
        for demand_element in self.demand_elements:
            cost += demand_element.calculate_cost()
        return cost + self.calculate_overloaded_links(32) * 10

    def calculate_link_coverage(self):
        link_dict = {}
        for demand_element in self.demand_elements:
            for path_element in demand_element.path_elements:
                for link in path_element.path.links:
                    if link in link_dict.keys():
                        link_dict[link] += 1
                    else:
                        link_dict[link] = 1
        return link_dict

    def calculate_overloaded_links(self, threshold):
        calc_dict = self.calculate_link_coverage()
        numerator = 0
        for value in calc_dict.values():
            if value > threshold:
                numerator += 1
        return numerator

    def get_demand_elements(self):
        return self.demand_elements

    def get_demand_element_from_index(self, index):
        return self.demand_elements[index]

    def add_demand_element(self, demand_gen):
        self.demand_elements.append(demand_gen)

    def mutate(self, probability):
        mutant = deepcopy(self)
        for el in mutant.get_demand_elements():
            el.mutate(probability)
        return mutant
