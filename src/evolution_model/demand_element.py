from src.evolution_model.path_element import PathElement
from src.evolution_model.transponders import Transponder100G, Transponder200G, Transponder400G
import random


class DemandElement:
    def __init__(self, demand, paths):
        self.bitrate_threshold = float(demand.demand_value)
        self.paths = paths
        self.path_elements = []
        self.generate_transponders()

    def generate_deterministic_transponders(self, transponder):
        # method for test purposes, cannot be used
        self.path_elements = []
        while self.calculate_provided_bitrate() < self.bitrate_threshold:
            self.path_elements.append(PathElement(self.paths[0], transponder))

    def generate_transponders(self):
        self.path_elements = []
        transponders_set = [Transponder100G(), Transponder200G(), Transponder400G()]
        while self.calculate_provided_bitrate() < self.bitrate_threshold:
            self.path_elements.append(PathElement(random.choice(self.paths), random.choice(transponders_set)))

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

    def count_transponders(self):
        transponders_dict = {}
        for path_element in self.path_elements:
            if path_element.transponder.transponder_type in transponders_dict.keys():
                transponders_dict[path_element.transponder.transponder_type] += 1
            else:
                transponders_dict[path_element.transponder.transponder_type] = 1
        return transponders_dict

    def mutate(self, prob):
        if random.uniform(0, 1) > prob:
            self.generate_transponders()
