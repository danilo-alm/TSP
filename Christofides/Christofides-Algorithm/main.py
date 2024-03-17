import os
import itertools

import src.utils as utils
from src.graph import Graph
from src.utils import create_graph_from_txt_file



if __name__ == '__main__':

    txt_file = r"Christofides-Algorithm\input\test.txt"
    debug_folder = r"output/6/"
    source_node = "1"
    debug = False

    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    else:
        print("Output Directory already exists")
        exit(1)

    # create graph from input txt file
    initial_g = utils.create_graph_from_txt_file(txt_file)
    if debug:
        print("Initial Graph:")
        utils.print_edges_with_weight(initial_g)
        initial_g.plot_graph(os.path.join(debug_folder, "graph.png"))

    # TODO : Validation of the graph: triangle inequality property

    # create a MST
    mst_graph = utils.get_mst(initial_g)
    if debug:
        print("\nMST:")
        utils.print_edges_with_weight(mst_graph)
        mst_graph.plot_graph(os.path.join(debug_folder, "mst.png"))

    mst_degrees = utils.get_degrees(mst_graph)
    if debug:
        print(f"\nMST degree : {mst_degrees}")

    odd_degrees = utils.get_nodes_odd_degrees(mst_degrees)
    if debug:
        print(f"\nMST odd degree : {odd_degrees}")

    subgraph = utils.create_subgraph(initial_g, odd_degrees)
    if debug:
        print("\nSubgraph:")
        utils.print_edges_with_weight(subgraph)
        subgraph.plot_graph(os.path.join(debug_folder, "subgraph.png"))

    minimum_perfect_match = utils.create_minimum_weight_perfect_matching(subgraph)
    if debug:
        print("\nMinimum weight perfect match:")
        utils.print_edges_with_weight(minimum_perfect_match)
        minimum_perfect_match.plot_graph(os.path.join(debug_folder, "minimum_perfect_match.png"))

    union_graph = utils.union_graphs(mst_graph, minimum_perfect_match)
    if debug:
        print("\nUnion graph details:")
        utils.print_edges_with_weight(union_graph)
        union_graph.plot_graph(os.path.join(debug_folder, "union_graph.png"))

    euler_tour_itr = union_graph.get_euler_tour(source_node)
    euler_tour = []
    for e in euler_tour_itr:
        euler_tour.append(e)

    if debug:
        print(f"\n Euler tour: {euler_tour}")
        euler_g = Graph()
        for e in euler_tour:
            euler_g.add_edge(e[0], e[1], initial_g.get_edge_weight(e[0], e[1]))
        euler_g.plot_graph(os.path.join(debug_folder, "euler_tour.png"))

    euler_tour = list(itertools.chain.from_iterable(list(euler_tour)))
    euler_tour = list(dict.fromkeys(euler_tour).keys())
    euler_tour.append(source_node)

    print(f"\nPath: {euler_tour}")
    if debug:
        final_path = Graph(di_graph=True)
        for i in range(len(euler_tour)-1):
            final_path.add_edge(euler_tour[i],
                                euler_tour[i+1],
                                initial_g.get_edge_weight(euler_tour[i], euler_tour[i+1]))
        final_path.plot_graph(os.path.join(debug_folder, "output.png"))

    total_weight = utils.get_total_cost(initial_g, euler_tour)
    print(f"Total traveling cost : {total_weight}")
