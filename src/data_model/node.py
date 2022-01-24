class Node:
    def __init__(self, name: str, longitude: float, latitude: float):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return f"{self.name} ({self.longitude} {self.latitude})"

    def __str__(self):
        return f"{self.name} ({self.longitude} {self.latitude})"
