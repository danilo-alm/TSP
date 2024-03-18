def tsp(data):
    # Construção do Grafo
    G = build_graph(data)
    print("Graph: ", G)

    # Construção de uma Árvore de Abrangência Mínima (Minimum Spanning Tree)
    MSTree = minimum_spanning_tree(G)
    print("MSTree: ", MSTree)

    # Identificação dos Vértices Ímpares na Árvore de Abrangência Mínima
    odd_vertexes = find_odd_vertexes(MSTree)
    print("Odd vertexes in MSTree: ", odd_vertexes)

    # Adição de Arestas de Emparelhamento de Peso Mínimo à Árvore de Abrangência Mínima
    minimum_weight_matching(MSTree, G, odd_vertexes)
    print("Minimum weight matching: ", MSTree)

    # Encontrar um Tour Euleriano no Grafo
    eulerian_tour = find_eulerian_tour(MSTree, G)
    print("Eulerian tour: ", eulerian_tour)

    # Cálculo do Comprimento do Tour
    current = eulerian_tour[0]
    path = [current]
    visited = [False] * len(eulerian_tour)
    visited[eulerian_tour[0]] = True
    length = 0

    for v in eulerian_tour:
        if not visited[v]:
            path.append(v)
            visited[v] = True

            length += G[current][v]
            current = v

    length +=G[current][eulerian_tour[0]]
    path.append(eulerian_tour[0])

    print("Result path: ", path)
    print("Result length of the path: ", length)

    return length, path


def get_length(x1, y1, x2, y2):
    # Calcula a distância entre dois pontos usando a fórmula da distância euclidiana
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1.0 / 2.0)



def build_graph(data):
    # Constrói um grafo completo representando todas as distâncias entre as cidades
    graph = {}
    for this in range(len(data)):
        for another_point in range(len(data)):
            if this != another_point:
                if this not in graph:
                    graph[this] = {}

                # Calcula a distância entre os pontos e a adiciona ao grafo
                graph[this][another_point] = get_length(data[this][0], data[this][1], data[another_point][0],
                                                        data[another_point][1])

    return graph



class UnionFind:
    # Implementação da estrutura de dados Union-Find para operações eficientes de união e busca
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        # Encontra o representante (raiz) do conjunto ao qual um objeto pertence
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # Encontra o representante (raiz) do conjunto e realiza compressão de caminho
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.parents)

    def union(self, *objects):
        # Realiza a união de dois conjuntos
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest



def minimum_spanning_tree(G):
    # Encontra uma árvore de abrangência mínima usando o algoritmo de Kruskal
    tree = []
    subtrees = UnionFind()
    for W, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v, W))
            subtrees.union(u, v)

    return tree



def find_odd_vertexes(MST):
    # Identifica os vértices com grau ímpar na árvore de abrangência mínima
    tmp_g = {}
    vertexes = []
    for edge in MST:
        if edge[0] not in tmp_g:
            tmp_g[edge[0]] = 0

        if edge[1] not in tmp_g:
            tmp_g[edge[1]] = 0

        tmp_g[edge[0]] += 1
        tmp_g[edge[1]] += 1

    for vertex in tmp_g:
        if tmp_g[vertex] % 2 == 1:
            vertexes.append(vertex)

    return vertexes



def minimum_weight_matching(MST, G, odd_vert):
    # Adiciona arestas de emparelhamento de peso mínimo ao grafo
    import random
    random.shuffle(odd_vert)

    while odd_vert:
        v = odd_vert.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)



def find_eulerian_tour(MatchedMSTree, G):
    # Encontra um tour euleriano no grafo
    neighbours = {}
    for edge in MatchedMSTree:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []

        if edge[1] not in neighbours:
            neighbours[edge[1]] = []

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])
        
    # encontra o circuito hamiltoniano
    start_vertex = MatchedMSTree[0][0]
    EP = [neighbours[start_vertex][0]]

    while len(MatchedMSTree) > 0:
        for i, v in enumerate(EP):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_matchedMST(MatchedMSTree, v, w)

            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
            EP.insert(i, w)

            v = w

    return EP



def remove_edge_from_matchedMST(MatchedMST, v1, v2):
    # Remove uma aresta do grafo
    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST






tsp([
    [0.0, 633.0, 257.0, 91.0, 412.0, 150.0, 80.0, 134.0, 259.0, 505.0, 353.0, 324.0, 70.0, 211.0, 268.0, 246.0, 121.0],
    [633.0, 0.0, 390.0, 661.0, 227.0, 488.0, 572.0, 530.0, 555.0, 289.0, 282.0, 638.0, 567.0, 466.0, 420.0, 745.0, 518.0],
    [257.0, 390.0, 0.0, 228.0, 169.0, 112.0, 196.0, 154.0, 372.0, 262.0, 110.0, 437.0, 191.0, 74.0, 53.0, 472.0, 142.0],
    [91.0, 661.0, 228.0, 0.0, 383.0, 120.0, 77.0, 105.0, 175.0, 476.0, 324.0, 240.0, 27.0, 182.0, 239.0, 237.0, 84.0],
    [412.0, 227.0, 169.0, 383.0, 0.0, 267.0, 351.0, 309.0, 338.0, 196.0, 61.0, 421.0, 346.0, 243.0, 199.0, 528.0, 297.0],
    [150.0, 488.0, 112.0, 120.0, 267.0, 0.0, 63.0, 34.0, 264.0, 360.0, 208.0, 329.0, 83.0, 105.0, 123.0, 364.0, 35.0],
    [80.0, 572.0, 196.0, 77.0, 351.0, 63.0, 0.0, 29.0, 232.0, 444.0, 292.0, 297.0, 47.0, 150.0, 207.0, 332.0, 29.0],
    [134.0, 530.0, 154.0, 105.0, 309.0, 34.0, 29.0, 0.0, 249.0, 402.0, 250.0, 314.0, 68.0, 108.0, 165.0, 349.0, 36.0],
    [259.0, 555.0, 372.0, 175.0, 338.0, 264.0, 232.0, 249.0, 0.0, 495.0, 352.0, 95.0, 189.0, 326.0, 383.0, 202.0, 236.0],
    [505.0, 289.0, 262.0, 476.0, 196.0, 360.0, 444.0, 402.0, 495.0, 0.0, 154.0, 578.0, 439.0, 336.0, 240.0, 685.0, 390.0],
    [353.0, 282.0, 110.0, 324.0, 61.0, 208.0, 292.0, 250.0, 352.0, 154.0, 0.0, 435.0, 287.0, 184.0, 140.0, 542.0, 238.0],
    [324.0, 638.0, 437.0, 240.0, 421.0, 329.0, 297.0, 314.0, 95.0, 578.0, 435.0, 0.0, 254.0, 391.0, 448.0, 157.0, 301.0],
    [70.0, 567.0, 191.0, 27.0, 346.0, 83.0, 47.0, 68.0, 189.0, 439.0, 287.0, 254.0, 0.0, 145.0, 202.0, 289.0, 55.0],
    [211.0, 466.0, 74.0, 182.0, 243.0, 105.0, 150.0, 108.0, 326.0, 336.0, 184.0, 391.0, 145.0, 0.0, 57.0, 426.0, 96.0],
    [268.0, 420.0, 53.0, 239.0, 199.0, 123.0, 207.0, 165.0, 383.0, 240.0, 140.0, 448.0, 202.0, 57.0, 0.0, 483.0, 153.0],
    [246.0, 745.0, 472.0, 237.0, 528.0, 364.0, 332.0, 349.0, 202.0, 685.0, 542.0, 157.0, 289.0, 426.0, 483.0, 0.0, 336.0],
    [121.0, 518.0, 142.0, 84.0, 297.0, 35.0, 29.0, 36.0, 236.0, 390.0, 238.0, 301.0, 55.0, 96.0, 153.0, 336.0, 0.0]
])
