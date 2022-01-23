import random
from src.evolution_model.transponders import Transponder100G
from src.evolution_model.demand_element import DemandElement


class Individual:
    def __init__(self, demands, demand_paths):
        self.demand_elements = []
        for demand in demands:
            paths = list(filter(lambda x: x.demand_id == demand.demand_id, demand_paths))
            self.demand_elements.append(DemandElement(demand, paths[0].paths))

    def calculate_cost(self):
        cost = 0
        for demand_element in self.demand_elements:
            cost += demand_element.calculate_cost()
        return cost

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

