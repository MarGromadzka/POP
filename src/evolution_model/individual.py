import random
from src.evolution_model.transponders import Transponder100G


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


class DemandElement:
    def __init__(self, demand, paths):
        self.bitrate_threshold = float(demand.demand_value)
        self.paths = paths
        self.path_elements = []
        self.init_transponders()

    def init_transponders(self):
        # method for test purposes, cannot be used
        self.path_elements = []
        while self.calculate_provided_bitrate() < self.bitrate_threshold:
            self.path_elements.append(PathElement(self.paths[0], Transponder100G()))

    def calculate_provided_bitrate(self):
        bitrate = 0
        for path_element in self.path_elements:
            bitrate += path_element.transponder.bitrate
        return bitrate

    def calculate_cost(self):
        cost = 0
        for path_element in self.path_elements:
            cost += path_element.transponder.cost
        return cost


class PathElement:
    def __init__(self, path, transponder):
        self.path = path
        self.transponder = transponder
