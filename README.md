## Comparação de Algoritmos por Base de Dados

| Algoritmo/Base de dados   | ATT48 (Tempo/Peso)       | DANTZIG42 (Tempo/Peso) | FRI26 (Tempo/Peso) | GR17 (Tempo/Peso) | P01 (Tempo/Peso) |
|---------------------------|--------------------------|------------------------|--------------------|-------------------|------------------|
| Força bruta               | Tempo / Peso             | Tempo / Peso           | Tempo / Peso       | Tempo / Peso      | Tempo / Peso     |
| Algoritmo de Dijkstra     | 0.0 / 37928              | 0.0 / 864              | 0.0 / 965          | 0.0 / 2178        | 0.0 / 291        |
| Algoritmo de Kruskal      | 0.0 / 27643.676498888937 | 0.0 / 559              | 0.0 / 960          | 0.0 / 2646        | 0.0 / 29         |
| Algoritmo de Christofides | 0.0 / 35789              | 0.0 / 559              | 0.0 / 960          | 0.0   / 2504      | 0.0   / 274      |

## Contato:

- **Arnaldo Lucas**: arnaldo.lucas@arapiraca.ufal.br
- **Danilo**: danilo.almeida@arapiraca.ufal.br
- **Everton Reis**: everton.reis@arapiraca.ufal.br
- **Marcos Paulo**: marcos.silva4@arapiraca.ufal.br


# Projeto: Problema do Caixeiro Viajante (PCV) 

Bem-vindo ao projeto do Problema do Caixeiro Viajante (PCV)! Este é um problema clássico de otimização combinatória no qual o objetivo é encontrar o caminho mais curto que visita todas as cidades uma vez e retorna à cidade de origem.


## Software necessário

O projeto foi testado usando Python 3.11.6.


## Instalação

[Jupyter Notebook](https://pypi.org/project/notebook/) é necessário para executar `main.ipynb`:
```
pip install notebook
```
Caso queira utilizar seu próprio script, nenhuma dependência externa é necessária.


## Como usar

_O arquivo `main.ipynb` já contém exemplos de uso._

### utils/distance_matrix.py

Fornece o objeto DistanceMatrix, que contém os seguintes métodos:
- `from_text`: retorna uma matriz de distância representada como um array numpy de duas dimensões; aceita uma *string* contendo as linhas da matriz.
- `from_text_file`: aceita o nome de um arquivo de texto, que será lido e passado para o método `from_text` para por fim retornar a matriz de distância.

### utils/tsp_solver.py

Fornece o objeto TSPSolver, que pode ser instanciado utilizando a matriz de distância obtida utilizando `DistanceMatrix` como parâmetro. Diversos métodos são fornecidos para encontrar o caminho mais curto:

- `brute_force`: explora todas as possíveis permutações de cidades e calcula a distância total para encontrar a solução mais eficiente. Vale ressaltar que o algoritmo de força bruta é viável apenas para um número pequeno de cidades (e.g. `data/FIVE`)

### utils/dijkstra_tsp.py

A classe `DijsktraTSP` implementa uma versão simplificada do algoritmo de Dijkstra para resolver o Problema do Caixeiro Viajante (PCV) de forma aproximada.

- `dijkstra_tsp`: este método estático calcula um caminho aproximado para o PCV a partir de uma matriz de distâncias entre cidades e um nó de partida. Ele utiliza o algoritmo de Dijkstra para encontrar o vizinho mais próximo de cada cidade, formando assim um caminho que visita cada cidade uma vez antes de retornar ao ponto de partida.

- `Parâmetros`: 
   - `matrix`: Uma matriz de distâncias entre cidades, onde `matrix[i][j]` representa a distância entre as cidades `i` e `j`.
   - `start`: O índice da cidade de partida.

- `Retorno`
   - Uma lista representando o caminho aproximado para o PCV, começando e terminando na cidade de partida.

- `bestDistance`:

Este método estático determina o caminho de menor distância entre todas as cidades, utilizando o método `dijkstra_tsp`, e imprime o caminho encontrado.

- `Parâmetros`: 
   - `matrizDistance`: Uma matriz de distâncias entre cidades.

### [utils/AGM.py](utils/AGM.py)

Esse programa em Python executa o algoritmo de Prim e de Kruskal para encontrar a Árvore Geradora Mínima para as bases ATT48, GR17 e P01. 
O custo é indicado no topo e a execução é imediata. 

## Próximos Passos:

O projeto será expandido com a implementação de outros algoritmos de resolução para o PCV para lidar com conjuntos de dados maiores de forma mais eficiente.


## Licença

Este projeto é licenciado sob a Licença Pública Geral GNU v3.0. Você é livre para modificar e distribuir este software de acordo com os termos da licença. Para obter mais detalhes, consulte o [texto completo da licença](https://www.gnu.org/licenses/gpl-3.0.html). Resumo da GNU GPL v3.0

- Você é livre para executar, modificar e compartilhar o software.
- Quaisquer modificações feitas devem ser liberadas sob a mesma licença durante a distribuição.
- Este software é distribuído sem qualquer garantia; consulte a licença para obter detalhes.

<hr>

# Algoritmo do Problema do Caixeiro Viajante (Traveling Salesman Problem - TSP)

Este projeto contém a implementação em Python do algoritmo do Problema do Caixeiro Viajante utilizando o Método de Christofides. O código foi desenvolvido para resolver instâncias do TSP representadas por um conjunto de coordenadas de pontos no plano.

## Funcionamento do Código

O código está estruturado da seguinte forma:

1. **`tsp(data)`**:
   - Função principal que executa o algoritmo TSP.
   - Recebe uma lista de coordenadas de pontos como entrada.
   - Divide o processo em etapas para resolver o TSP, incluindo a construção do grafo, criação de uma Árvore de Abrangência Mínima, identificação de vértices ímpares, emparelhamento de peso mínimo, busca de um Tour Euleriano e cálculo do comprimento do tour.

2. **`build_graph(data)`**:
   - Constrói um grafo completo representando todas as distâncias entre as cidades (pontos) utilizando a distância euclidiana.

3. **`UnionFind`**:
   - Implementação da estrutura de dados Union-Find para operações eficientes de união e busca.

4. **`minimum_spanning_tree(G)`**:
   - Utiliza o algoritmo de Kruskal para encontrar uma Árvore de Abrangência Mínima no grafo G.

5. **`find_odd_vertexes(MST)`**:
   - Identifica os vértices com grau ímpar na Árvore de Abrangência Mínima.

6. **`minimum_weight_matching(MST, G, odd_vert)`**:
   - Adiciona arestas de emparelhamento de peso mínimo à Árvore de Abrangência Mínima.

7. **`find_eulerian_tour(MatchedMSTree, G)`**:
   - Encontra um tour euleriano no grafo, combinando a Árvore de Abrangência Mínima e o emparelhamento de peso mínimo.

8. **`remove_edge_from_matchedMST(MatchedMST, v1, v2)`**:
   - Remove uma aresta do grafo MatchedMST.


## Etapas Básicas:

1. **Encontre uma árvore geradora mínima (T):**
   - Utilize um algoritmo como o algoritmo de Kruskal ou Prim para encontrar a árvore geradora mínima do grafo.

2. **Encontre vértices em T com grau ímpar (O):**
   - Identifique os vértices na árvore geradora mínima que possuem grau ímpar.

3. **Encontre arestas de correspondência de peso mínimo (M) para T:**
   - Para cada par de vértices ímpares, encontre a aresta de peso mínimo que os conecta.

4. **Construa um circuito Euleriano usando as arestas de M e T:**
   - Utilize um algoritmo para encontrar um circuito Euleriano no grafo formado pelas arestas de M e T.

5. **Faça um circuito Hamiltoniano pulando vértices repetidos:**
   - A partir do circuito Euleriano obtido, construa um circuito Hamiltoniano pulando vértices repetidos.

## Utilização

Para executar o algoritmo, basta chamar a função `tsp(data)` e passar como argumento uma lista de coordenadas de pontos no plano. Por exemplo:

```python
tsp([
    [0.0, 633.0, 257.0, 91.0, 412.0, ...],
    [633.0, 0.0, 390.0, 661.0, 227.0, ...],
    ...
])



