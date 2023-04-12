from pathfinder.pathfinder import PathFinder
from pathfinder.AStar import AStar
from pathfinder.graph import graph
from pathfinder.city import City
from pathfinder.heuristics import heuristics

# pf = PathFinder(graph)
# pf.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

astr = AStar(graph, heuristics)
astr.get_shortest_path(City.BORDEAUX, City.STRASBOURG)