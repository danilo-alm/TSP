
def dijkstra_tsp(matrix, start):
    num_cities = len(matrix)
    visited = set([start])
    path = [start]
    current = start
    while len(visited) < num_cities:
        nearest_neighbor = None
        nearest_distance = float('inf')
        for neighbor in range(num_cities):
            if neighbor not in visited:
                distance = matrix[current][neighbor]
                if distance < nearest_distance:
                    nearest_neighbor = neighbor
                    nearest_distance = distance
        if nearest_neighbor is not None:
            path.append(nearest_neighbor)
            visited.add(nearest_neighbor)
            current = nearest_neighbor
        else:
            break
    path.append(start)  # Volta ao vértice inicial
    return path

# Exemplo de uso
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
#start_city = 0

num_cities = len(distances)

countFinal=100000
tourFinal = []

for start_node in range(num_cities):
    countAux=0
    tour = dijkstra_tsp(distances, start_node)
    for i in range(len(tour)-1):
        countAux+=distances[tour[i]][tour[i+1]]
    if countAux<countFinal:
        countFinal=countAux
        tourFinal=tour

print("Caminho aproximado do PCV:", tourFinal)

