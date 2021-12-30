from Node import Node
from Link import Link
from Demand import Demand

with open('nodes.txt', 'r') as file:
    lines = [line.rstrip("\n") for line in file]
    nodes = []
    for line in lines:
        splitted_line = line.split(' ')
        nodes.append(Node(splitted_line[0], float(splitted_line[2]), float(splitted_line[3])))

with open('links.txt', 'r') as file:
    lines = [line.rstrip("\n") for line in file]
    links = []
    for line in lines:
        sl = line.split(' ')
        links.append(Link(sl[0], sl[2], sl[3], float(sl[5]), float(sl[6]), float(sl[7]), float(sl[8]), float(sl[10]), float(sl[11])))

with open('demands.txt', 'r') as file:
    lines = [line.rstrip("\n") for line in file]
    demands = []
    for line in lines:
        sl = line.split(' ')
        demands.append(Demand(sl[0], sl[2], sl[3], sl[5], sl[6], sl[7]))
