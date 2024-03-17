# Algoritmo de Christofides para o Problema do Caixeiro Viajante (PCV)

## Introdução

O Problema do Caixeiro Viajante (PCV) é um problema clássico de otimização em ciência da computação e matemática. Dado um conjunto de cidades e as distâncias entre elas, o objetivo é encontrar a rota mais curta possível que visite cada cidade exatamente uma vez e retorne à cidade de origem. O PCV é conhecido por ser um problema NP-difícil, o que significa que não há um algoritmo conhecido de tempo polinomial que possa resolvê-lo de forma ótima para todas as instâncias.

O algoritmo de Christofides é um algoritmo aproximado projetado para encontrar uma solução para o PCV que está garantida de estar dentro de um fator de 1,5 do comprimento da solução ótima. Foi proposto por Nicos Christofides em 1976 e é baseado em vários passos-chave, incluindo a construção de uma árvore geradora mínima, a identificação de vértices de grau ímpar, o cálculo de um emparelhamento perfeito de peso mínimo e a construção de um circuito hamiltoniano.

## Espaço Métrico

Antes de entrar nos detalhes do algoritmo, é importante observar que o algoritmo de Christofides é projetado para espaços métricos. Um espaço métrico é uma construção matemática onde a função de distância entre quaisquer dois pontos (cidades, neste caso) satisfaz as seguintes propriedades:

1. **Positividade**: A distância entre quaisquer dois pontos é sempre não negativa.
2. **Simetria**: A distância do ponto A ao ponto B é a mesma que a distância do ponto B ao ponto A.
3. **Reflexividade**: A distância de um ponto a ele mesmo é sempre zero.
4. **Desigualdade Triangular**: A soma das distâncias de dois lados de um triângulo é maior ou igual à distância do terceiro lado.

## Passos do Algoritmo

O algoritmo de Christofides pode ser dividido em vários passos-chave:

1. **Árvore Geradora Mínima (AGM)**: Construir uma árvore geradora mínima usando um algoritmo adequado como Prim ou Kruskal.
2. **Vértices de Grau Ímpar**: Identificar os vértices na AGM com graus ímpares (ou seja, número ímpar de arestas incidentes a eles).
3. **Emparelhamento Perfeito de Peso Mínimo**: Encontrar um emparelhamento perfeito de peso mínimo para os vértices de grau ímpar.
4. **Multigrafo Conectado**: Combinar a árvore geradora mínima e o emparelhamento perfeito de peso mínimo para formar um multigrafo conectado.
5. **Circuito Euleriano**: Encontrar um circuito euleriano no multigrafo conectado.
6. **Circuito Hamiltoniano**: Converter o circuito euleriano em um circuito hamiltoniano, evitando vértices repetidos.


## Complexidade Temporal

A complexidade temporal do algoritmo de Christofides pode ser analisada da seguinte forma:

- Construção da árvore geradora mínima: O(n^2) ou O(n log n) dependendo do algoritmo escolhido.
- Identificação de vértices de grau ímpar: O(n).
- Cálculo do emparelhamento perfeito de peso mínimo: O(n^3) usando algoritmos como o algoritmo Blossom.
- Combinação dos componentes e busca de circuitos eulerianos e hamiltonianos: O(n) ou O(n log n) dependendo da implementação.

No geral, a complexidade temporal do algoritmo é O(n^3) devido ao passo que envolve o cálculo do emparelhamento perfeito de peso mínimo, que domina o custo computacional.


