import networkx as nx

def dijkstra_tsp(graph, start):
    visited = set([start])
    path = [start]
    current = start
    while len(visited) < len(graph.nodes):
        nearest_neighbor = None
        nearest_distance = float('inf')
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                distance = nx.dijkstra_path_length(graph, current, neighbor, weight='weight')
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
G = nx.Graph()
""" G.add_weighted_edges_from([(0, 8, 39), (8, 0, 45), (39, 45, 0)])
 """

distances = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]

""" G.add_weighted_edges_from(distances) """

start_node = 0

tour = dijkstra_tsp(distances, start_node)
print("Caminho aproximado do PCV:", tour)


