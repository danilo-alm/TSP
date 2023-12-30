from itertools import permutations

class TSPSolver:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def __get_tour_distance(self, tour):
        return ( 
            sum(self.distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
                + self.distance_matrix[tour[-1]][tour[0]]
        )

    def brute_force(self):
        num_cities = len(self.distance_matrix)
        all_permutations = permutations(range(num_cities))
        
        best_tour = None
        best_distance = float('inf')
        
        for tour in all_permutations:
            total_distance = self.__get_tour_distance(tour)

            if total_distance < best_distance:
                best_distance = total_distance
                best_tour = tour
        
        return best_tour, best_distance