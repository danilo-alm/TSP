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
                            for j in range(i+1, len(parts)):
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


# Exemplo de uso:
if __name__ == "__main__":
    coordenadas_att48 = SolucionadorTSP.ler_coordenadas("../data/ATT48/att48.tsp")
    coordenadas_gr17 = SolucionadorTSP.ler_coordenadas("../data/GR17/gr17.tsp")

    print(coordenadas_att48)
    print(coordenadas_gr17)

    # Criar instâncias dos Solucionadores TSP
    solucionador_att48 = SolucionadorTSP(coordenadas_att48)
    solucionador_gr17 = SolucionadorTSP(coordenadas_gr17)

    # Imprimir as arestas da Árvore Geradora Mínima para o att48
    print("\nArestas da Árvore Geradora Mínima para att48:")
    agm_arestas_att48 = solucionador_att48.agm_kruskal()
    for aresta in agm_arestas_att48:
        print(aresta)

    # Imprimir as arestas da Árvore Geradora Mínima para o gr17
    print("\nArestas da Árvore Geradora Mínima para gr17:")
    agm_arestas_gr17 = solucionador_gr17.agm_kruskal()
    for aresta in agm_arestas_gr17:
        print(aresta)
