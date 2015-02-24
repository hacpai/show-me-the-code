class TSP(object):
    """Represents a TSP object.
    """

    def __init__(self, distance, cities):
        self.distance = distance
        self.path = []
        self.cities = 'ABCD'

    def nearest_city(self, source, remain_cities):
        """Return the city that the nearest city source.
        """
        min_distance = 10000
        for destination in remain_cities:
            city_to_city = source, destination
            try:
                if self.distance[city_to_city] < min_distance:
                    min_distance = self.distance[city_to_city]
                    res = destination
            except KeyError:
                continue
        return res

    def compute_path(self):
        """Computes the path about TSP.

        assume it works in City A.
        """
        self.path.append('A')
        remain_cities = self.cities.replace('A', '')
        while len(remain_cities) > 0:
            city = self.nearest_city(self.path[-1], remain_cities)
            remain_cities = remain_cities.replace(city, '')
            self.path.append(city)


if __name__ == '__main__':

    distance = {('A', 'B'): 2, ('A', 'C'): 6, ('A', 'D'): 5,
                ('B', 'A'): 2, ('B', 'C'): 4, ('B', 'D'): 4,
                ('C', 'A'): 6, ('C', 'B'): 4, ('C', 'D'): 2,
                ('D', 'A'): 5, ('D', 'B'): 4, ('D', 'C'): 2}
    cities = 'ABCD'

    tsp = TSP(distance, cities)
    tsp.compute_path()
    print tsp.path
