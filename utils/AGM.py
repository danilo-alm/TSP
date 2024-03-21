import datetime
from itertools import permutations
import math


class ConjuntoDisjunto:
    def __init__(self, n):
        self.pai = [i for i in range(n)]
        self.rank = [0] * n

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x, y):
        x_raiz = self.encontrar(x)
        y_raiz = self.encontrar(y)

        if x_raiz == y_raiz:
            return False

        if self.rank[x_raiz] < self.rank[y_raiz]:
            self.pai[x_raiz] = y_raiz
        elif self.rank[x_raiz] > self.rank[y_raiz]:
            self.pai[y_raiz] = x_raiz
        else:
            self.pai[y_raiz] = x_raiz
            self.rank[x_raiz] += 1

        return True


class SolucionadorTSP:
    def __init__(self, coordenadas_param):
        self.coordenadas = coordenadas_param
        self.matriz_distancias = self.calcular_matriz_distancias()

    def obter_distancia_tour(self, tour):
        return (
                sum(self.matriz_distancias[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
                + self.matriz_distancias[tour[-1]][tour[0]]
        )

    def forca_bruta(self):
        num_cidades = len(self.coordenadas)
        todas_permutacoes = permutations(range(num_cidades))

        melhor_tour = None
        melhor_distancia = float('inf')

        for tour in todas_permutacoes:
            distancia_total = self.obter_distancia_tour(tour)

            if distancia_total < melhor_distancia:
                melhor_distancia = distancia_total
                melhor_tour = tour

        return melhor_tour, melhor_distancia

    # AGM de Kruskal
    def agm_kruskal(self):
        num_cidades = len(self.coordenadas)
        arestas = []

        for i in range(num_cidades):
            for j in range(i + 1, num_cidades):
                if isinstance(self.coordenadas[i], int) and isinstance(self.coordenadas[j], int):
                    distancia = self.coordenadas[i]
                else:
                    x1, y1 = self.coordenadas[i]
                    x2, y2 = self.coordenadas[j]
                    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                arestas.append((i, j, distancia))

        arestas.sort(key=lambda x: x[2])
        arestas_agm = []
        conjunto_disjunto = ConjuntoDisjunto(num_cidades)

        for aresta_grafo in arestas:
            u, v, peso = aresta_grafo  # Desempacotamento da tupla
            if conjunto_disjunto.unir(u, v):
                arestas_agm.append(aresta_grafo)

        return arestas_agm

    # AGM de Prim
    def agm_prim(self):
        num_cidades = len(self.coordenadas)
        arvore_geradora = []

        # Define o vértice inicial aleatório
        visitados = [False] * num_cidades
        visitados[0] = True

        while len(arvore_geradora) < num_cidades - 1:
            menor_distancia = float('inf')
            aresta_mais_curta = None

            for i in range(num_cidades):
                if visitados[i]:
                    for j in range(num_cidades):
                        if not visitados[j]:
                            distancia = self.matriz_distancias[i][j]
                            if distancia < menor_distancia:
                                menor_distancia = distancia
                                aresta_mais_curta = (i, j, distancia)

            if aresta_mais_curta:
                u, v, peso = aresta_mais_curta
                arvore_geradora.append(aresta_mais_curta)
                visitados[v] = True

        return arvore_geradora

    def custo_arvore(self, arestas):
        return sum(aresta_[2] for aresta_ in arestas)

    @classmethod
    def ler_coordenadas(cls, arquivo):
        coordenadas = []
        with open(arquivo, 'r') as file:
            coord_section = False
            edge_weight_section = False
            for line in file:
                if line.startswith("NODE_COORD_SECTION"):
                    coord_section = True
                    continue
                elif line.startswith("EDGE_WEIGHT_SECTION"):
                    edge_weight_section = True
                    coord_section = False
                    continue
                elif line.startswith("EOF"):
                    break
                if coord_section:
                    parts = line.split()
                    if len(parts) >= 3:
                        city, x, y = map(float, parts[0:3])
                        coordenadas.append((x, y))
                elif edge_weight_section:
                    parts = line.split()
                    for i in range(len(parts)):
                        if parts[i].isdigit():
                            for j in range(i + 1, len(parts)):
                                if parts[j].isdigit():
                                    distance = int(parts[j])
                                    coordenadas.append(distance)
                                    break
                            break
        return coordenadas

    def calcular_matriz_distancias(self):
        num_cidades = len(self.coordenadas)
        matriz_distancias = [[0] * num_cidades for _ in range(num_cidades)]

        for i in range(num_cidades):
            for j in range(i + 1, num_cidades):
                if isinstance(self.coordenadas[i], int) and isinstance(self.coordenadas[j], int):
                    distancia = self.coordenadas[i]
                else:
                    x1, y1 = self.coordenadas[i]
                    x2, y2 = self.coordenadas[j]
                    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                matriz_distancias[i][j] = distancia
                matriz_distancias[j][i] = distancia

        return matriz_distancias


if __name__ == "__main__":
    coordenadas_att48 = SolucionadorTSP.ler_coordenadas("../data/ATT48/att48.tsp")
    coordenadas_gr17 = SolucionadorTSP.ler_coordenadas("../data/GR17/gr17.tsp")
    coordenadas_p01 = SolucionadorTSP.ler_coordenadas("../data/P01/p01.tsp")

    print(coordenadas_att48)
    print(coordenadas_gr17)
    print(coordenadas_p01)

    # Criar instâncias dos Solucionadores TSP
    t1 = datetime.date.today()
    solucionador_att48 = SolucionadorTSP(coordenadas_att48)
    t2 = datetime.date.today()
    print("Tempo: " + str(t1 - t2))

    t1 = datetime.date.today()
    solucionador_gr17 = SolucionadorTSP(coordenadas_gr17)
    t2 = datetime.date.today()
    print("Tempo: " + str(t1 - t2))

    t1 = datetime.date.today()
    solucionador_p01 = SolucionadorTSP(coordenadas_p01)
    t2 = datetime.date.today()
    print("Tempo: " + str(t1 - t2))

    # Imprimir as arestas da Árvore Geradora Mínima para o att48
    print("\nArestas da Árvore Geradora Mínima para att48:")
    agm_arestas_att48 = solucionador_att48.agm_kruskal()
    for aresta in agm_arestas_att48:
        print(aresta)
    print("Custo total da AGM de Kruskal para att48:", solucionador_att48.custo_arvore(agm_arestas_att48))

    # Imprimir as arestas da Árvore Geradora Mínima para o gr17
    print("\nArestas da Árvore Geradora Mínima para gr17:")
    agm_arestas_gr17 = solucionador_gr17.agm_kruskal()
    for aresta in agm_arestas_gr17:
        print(aresta)
    print("Custo total da AGM de Kruskal para gr17:", solucionador_gr17.custo_arvore(agm_arestas_gr17))

    # Imprimir as arestas da Árvore Geradora Mínima para o att48 usando Prim
    print("\nArestas da Árvore Geradora Mínima para att48 usando Prim:")
    agm_arestas_att48_prim = solucionador_att48.agm_prim()
    for aresta in agm_arestas_att48_prim:
        print(aresta)
    print("Custo total da AGM de Prim para att48:", solucionador_att48.custo_arvore(agm_arestas_att48_prim))

    # Imprimir as arestas da Árvore Geradora Mínima para o gr17 usando Prim
    print("\nArestas da Árvore Geradora Mínima para gr17 usando Prim:")
    agm_arestas_gr17_prim = solucionador_gr17.agm_prim()
    for aresta in agm_arestas_gr17_prim:
        print(aresta)
    print("Custo total da AGM de Prim para gr17:", solucionador_gr17.custo_arvore(agm_arestas_gr17_prim))

    # Imprimir as arestas da Árvore Geradora Mínima para o p01 usando Prim
    print("\nArestas da Árvore Geradora Mínima para p01 usando Prim:")
    agm_arestas_p01_prim = solucionador_p01.agm_prim()
    for aresta in agm_arestas_p01_prim:
        print(aresta)
    print("Custo total da AGM de Prim para p01:", solucionador_p01.custo_arvore(agm_arestas_p01_prim))