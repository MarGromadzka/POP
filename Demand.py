class Demand:

    def __init__(self, demand_id: str, source: str, target: str, routing_unit: int, demand_value: float, max_path_length):
        self.demand_id = demand_id
        self.source = source
        self.target = target
        self.routing_unit = routing_unit
        self.demand_value = demand_value
        self.max_path_length = max_path_length
