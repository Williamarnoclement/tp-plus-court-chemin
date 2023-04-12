from pathfinder.pathfinder import PathFinder
from pathfinder.city import City
from pathfinder.graph import graph
from pathfinder.path import Path

class AStar(PathFinder):
    cities = {}
    cities_to_visit = []
    cities_visited = []
    def __init__(self, graph, heuristics) -> None:
        self.graph = graph
        self.heuristics = heuristics
        PathFinder.__init__(self, graph) 