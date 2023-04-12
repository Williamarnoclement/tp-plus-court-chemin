from pathfinder.city import City
from pathfinder.spfa import SPFA
from pathfinder.graph import spfa_graph

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 15,
      "steps": [City.BORDEAUX, City.NANTES, City.RENNES, City.ROUEN, City.PARIS, City.ORLEANS, City.STRASBOURG]
    }
  },
  {
    "start": City.NANTES,
    "end": City.LILLE,
    "path": {
      "total": 15,
      "steps": [City.NANTES, City.RENNES, City.ROUEN, City.PARIS, City.ORLEANS, City.STRASBOURG, City.LILLE]
    }
  },
  {
    "start": City.BORDEAUX,
    "end": City.LYON,
    "path": {
      "total": -25,
      "steps": [City.BORDEAUX, City.TOULOUSE, City.LYON]
    }
  },
  {
    "start": City.NANTES,
    "end": City.ORLEANS,
    "path": {
      "total": -50,
      "steps": [City.NANTES, City.RENNES, City.ROUEN, City.PARIS, City.ORLEANS]
    }
  }
]

test_spfa = SPFA(spfa_graph)

error = False

for test in tests:
    print("\033[34m-> Testing SPFA path from", test["start"], "to", test["end"], "\033[0m")
    spfa_path = test_spfa.get_shortest_path(test["start"], test["end"])

    if spfa_path == test["path"]:
        print("\033[92m✓ Test OK for SPFA path from", test["start"], "to", test["end"], "\033[0m")
    else:
        print("\033[91mError for SPFA path from", test["start"], "to", test["end"], "\033[0m")
        print("Expected", test["path"])
        print("Got ", spfa_path)
        error = True

print('\033[92m✓ OK' if not error else '\033[91m❌ KO')

