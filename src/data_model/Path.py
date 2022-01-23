class Path:
    def __init__(self, path_id, demand_id, links):
        self.path_id = path_id
        self.demand_id = demand_id
        self.links = links

    def __str__(self):
        return f"{self.path_id}: {[link for link in self.links]}"

    def __repr__(self):
        return f"{self.path_id}: {[link for link in self.links]}"
