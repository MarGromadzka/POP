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
        # method for test purposes, cannot be used
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

    # def mutate(self, prob):
    #     if random.uniform(0, 1) > prob:
    #         self.merge_transponders("100G")

    # def merge_transponders(self, transponder_type):
    #     path_removed = self.remove_transponders(transponder_type, 2)
    #     self.add_transponder("200G", random.choice(path_removed))

    # def remove_transponders(self, transformer_type, count):
    #     counter = 0
    #     path_removed = []
    #     indices_to_remove = []
    #     for i, path_element in enumerate(self.path_elements):
    #         if (path_element.transponder.transponder_type == transformer_type) and (counter <= count):
    #             indices_to_remove.append(i)
    #             counter += 1
    #             path_removed.append(path_element.path)
    #     removed_counter = 0
    #     for index in indices_to_remove:
    #         self.path_elements.pop(index - removed_counter)
    #         removed_counter += 1
    #     return path_removed
    #
    # def add_transponder(self, transponder_type, path):
    #     if transponder_type == "100G":
    #         self.path_elements.append(PathElement(path, Transponder100G()))
    #     if transponder_type == "200G":
    #         self.path_elements.append(PathElement(path, Transponder200G()))
    #     if transponder_type == "400G":
    #         self.path_elements.append(PathElement(path, Transponder400G()))


        # ACHTUNG - wymyślić tu jakąś inną logikę
        # jeśli są dwa transpondery o takim samym G to merguj
        # rozbij transponder na mniejsze
