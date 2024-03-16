import networkx as nx
import numpy as np

# Matriz de adjacência com os pesos das arestas
adjacency_matrix = np.array([
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
])

# Criar um grafo não direcionado
G = nx.Graph()

# Adicionar as arestas ao grafo
num_nodes = adjacency_matrix.shape[0]
for i in range(num_nodes):
    for j in range(i+1, num_nodes):  # Apenas uma metade da matriz, já que o grafo é não direcionado
        if adjacency_matrix[i][j] != 0:  # Se houver uma conexão (aresta)
            G.add_edge(i, j, weight=adjacency_matrix[i][j])  # Adiciona a aresta com o peso

# Calcular o caminho mais curto para o PCV a partir de cada nó
shortest_paths = {}
for start_node in range(num_nodes):
    for end_node in range(num_nodes):
        if start_node == end_node:
            continue
        else:
            shortest_path = nx.dijkstra_path(G, start_node, weight='weight', target=end_node)
            shortest_paths[start_node] = shortest_path

    
# Encontrar o caminho mais curto entre todos os nós
best_tour = None
best_length = float('inf')
for start_node, path in shortest_paths.items():
    length = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    if length < best_length:
        best_length = length
        best_tour = path

print("Caminho aproximado do PCV:", best_tour)
