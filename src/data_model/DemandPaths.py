class DemandPaths:

    def __init__(self, demand_id):
        self.demand_id = demand_id
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)

    def __str__(self):
        return f"{self.demand_id} paths: {[path for path in self.paths]}"

    def __repr__(self):
        return f"{self.demand_id} paths: {[path for path in self.paths]}"