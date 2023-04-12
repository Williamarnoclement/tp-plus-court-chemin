from pathfinder.city import City
from pathfinder.graph import graph
from pathfinder.path import Path

class PathFinder:
    cities = {}
    cities_to_visit = []
    cities_visited = []
    def __init__(self, graph) -> None:
        self.graph = graph
        
    def get_shortest_path(self, start: City, end: City):
        # on démarre avec l'initialisation de la 
        # distance de chaque ville relativement à la ville 
        # de départ
        for city in self.graph:
            self.cities[city] = {"distance": float("inf")}
        self.cities[start]["distance"] = 0
        self.cities_to_visit.append(start)
        while (len(self.cities_to_visit) > 0):
            closest_city: City = self.cities_to_visit[0]
            for city in self.cities_to_visit:
                if (self.cities[city]["distance"] < self.cities[closest_city]["distance"] and city not in self.cities_visited):
                    closest_city = city
            #print("Nous allons visiter ", closest_city)
            #if (closest_city == end):
                #print("Nous sommes arrivés d'une nouvelle manière!")
            for key, value in self.graph[closest_city].items():
                if self.cities[closest_city]["distance"] + value < self.cities[key]["distance"]:
                    #print("On attribue une nouvelle distance à la ville connectée")
                    self.cities[key]["distance"] = self.cities[closest_city]["distance"] + value
                    self.cities[key]["from"] = closest_city
                #print(key, " ", self.cities[key]["distance"])
                if (key not in self.cities_visited):
                    self.cities_to_visit.append(key)
                #print(self.cities_to_visit)
            self.cities_visited.append(closest_city)
            self.cities_to_visit.remove(closest_city)
        final_path : Path = {
            "total" : 0,
            "steps" : []
        }
        #print(self.cities)
        closest_city: City = end
        founded_path: bool = False
        final_path["total"] = self.cities[end]["distance"]

        while(founded_path == False):
            # final_path["steps"].append(closest_city)
            final_path["steps"].insert(0, closest_city)
            #print (final_path)
            if closest_city == start:
                break
            print(self.cities[closest_city])
            closest_city = self.cities[closest_city]["from"]
        print("final_path__________________________________")
        print(final_path)
        return final_path

# pf = PathFinder(graph)
# pf.get_shortest_path(City.BORDEAUX, City.STRASBOURG)