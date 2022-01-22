class Link:

    def __init__(self,
                 link_id: str,
                 source: str,
                 target: str,
                 pre_installed_capacity: float,
                 pre_installed_capacity_cost: float,
                 routing_cost: float,
                 setup_cost: float,
                 module_capacity: float,
                 module_cost: float):
        self.link_id = link_id
        self.source = source
        self.target = target
        self.pre_installed_capacity = pre_installed_capacity
        self.pre_installed_capacity_cost = pre_installed_capacity_cost
        self.routing_cost = routing_cost
        self.setup_cost = setup_cost
        self.module_capacity = module_capacity
        self.module_cost = module_cost


    def __repr__(self):
        return f"{self.link_id} ({self.source} {self.target}"

    def __str__(self):
        return f"{self.link_id} ({self.source} {self.target}"