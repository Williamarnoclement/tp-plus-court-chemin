from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.graph import graph
from pathfinder.heuristics import heuristics

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 59,
      "steps": [City.BORDEAUX, City.ORLEANS, City.DIJON, City.STRASBOURG]
    }
  },
  {
    "start": City.LILLE,
    "end": City.STRASBOURG,
    "path": {
      "total": 29,
      "steps": [City.LILLE, City.STRASBOURG]
    }
  },
  {
    "start": City.RENNES,
    "end": City.STRASBOURG,
    "path": {
      "total": 50,
      "steps": [City.RENNES, City.ROUEN, City.PARIS, City.STRASBOURG]
    }
  }
]

error: bool = False

test_pathfinder = AStar(graph, heuristics)

for test in tests:
    print("\033[34m-> Testing Pathfinder path from", test["start"], "to", test["end"], "\033[0m")
    pathfinder_path = test_pathfinder.get_shortest_path(test["start"], test["end"])

    if pathfinder_path == test["path"]:
        print("\033[92m✓ Test OK for Pathfinder path from", test["start"], "to", test["end"], "\033[0m")
    else:
        print("\033[91mError for Pathfinder path from", test["start"], "to", test["end"], "\033[0m")
        print("Expected", test["path"])
        print("Got ", pathfinder_path)
        error = True

print('\033[92m✓ OK' if not error else '\033[91m❌ KO')
