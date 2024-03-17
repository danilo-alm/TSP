import numpy as np
import networkx as nx
from tkinter import filedialog as fd

def open_file_selection():
    return fd.askopenfile()

# Construir matriz de distância das cidades
def build_graph_matrix():
    file = open_file_selection()

    dist_matrix = []
    for line in file:
        row = [float(x) for x in line.split()]
        dist_matrix.append(row)
    file.close()

    return dist_matrix

# Função para encontrar a árvore geradora mínima usando o algoritmo de Prim
def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

#Função para encontrar os vértices com grau ímpar
def find_odd_vertices(graph):
    odd_vertices = []
    for node in graph.nodes():
        if graph.degree(node) % 2 != 0:
            odd_vertices.append(node)
    return odd_vertices

# Função para encontrar a correspondência perfeita de peso mínimo de vértices ímpares usando algoritmo guloso
def minimum_weight_matching(graph, odd_vertices):
    min_weight_matching = nx.algorithms.matching.max_weight_matching(graph, maxcardinality=False)
    min_weight_matching_edges = [(u, v) for u, v in min_weight_matching]
    return min_weight_matching_edges

# Função para construir um multigrafo a partir da árvore geradora mínima e correspondência de peso mínimo
def construct_multigraph(graph, mst, matching_edges):
    multigraph = nx.MultiGraph(graph)
    multigraph.add_edges_from(matching_edges)
    return multigraph

# Função para encontrar um circuito Euleriano no multigrafo
def eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

# Function to find a Hamiltonian circuit from the Eulerian circuit
def christofides_algorithm(graph):
    # Etapa 1: calcular a árvore geradora mínima
    mst = minimum_spanning_tree(graph)

    #  Etapa 2: Encontre vértices com grau ímpar
    odd_vertices = find_odd_vertices(mst)

    # Etapa 3: Encontre a correspondência perfeita de peso mínimo de vértices ímpares
    min_weight_matching_edges = minimum_weight_matching(graph, odd_vertices)

    # Step 4: Etapa 4: construir um multigrafo
    multigraph = construct_multigraph(graph, mst, min_weight_matching_edges)

    # Etapa 5: Encontre o circuito Euleriano no multigrafo
    eulerian_path = eulerian_circuit(multigraph)

    # Step 6: Remova duplicatas do caminho Euleriano para obter o caminho Hamiltoniano
    hamiltonian_path = list(dict.fromkeys([node for node, _ in eulerian_path]))

    # Etapa 7: Retorna o circuito hamiltoniano
    return hamiltonian_path

# Example usage:
if __name__ == "__main__":
    # Build graph matrix
    graph_matrix = build_graph_matrix()

    # Convert matrix to graph
    graph = nx.from_numpy_array(np.array(graph_matrix))

    # Run Christofides algorithm
    hamiltonian_path = christofides_algorithm(graph)

    print("Approximate solution (Hamiltonian circuit):", hamiltonian_path)
    print("Menor caminho tem:", len(hamiltonian_path), "vertices")
