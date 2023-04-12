from pathfinder.city import City
from pathfinder.pathfinder import PathFinder
from pathfinder.graph import graph

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 57,
      "steps": [City.BORDEAUX, City.ORLEANS, City.PARIS, City.STRASBOURG]
    }
  },
  {
    "start": City.STRASBOURG,
    "end": City.BORDEAUX,
    "path": {
      "total": 57,
      "steps": [City.STRASBOURG, City.PARIS, City.ORLEANS, City.BORDEAUX]
    }
  },
  {
    "start": City.LILLE,
    "end": City.TOULOUSE,
    "path": {
      "total": 58,
      "steps": [City.LILLE, City.PARIS, City.ORLEANS, City.BORDEAUX, City.TOULOUSE]
    }
  },
  {
    "start": City.LILLE,
    "end": City.NANTES,
    "path": {
      "total": 31,
      "steps": [City.LILLE, City.ROUEN, City.NANTES]
    }
  },
  {
    "start": City.LYON,
    "end": City.MARSEILLE,
    "path": {
      "total": 18,
      "steps": [City.LYON, City.MARSEILLE]
    }
  }
]

error: bool = False

test_pathfinder = PathFinder(graph)

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
