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


## Contato:

- **Arnaldo Lucas**: arnaldo.lucas@arapiraca.ufal.br
- **Danilo**: danilo.almeida@arapiraca.ufal.br
- **Everton Reis**: everton.reis@arapiraca.ufal.br
- **Marcos Paulo**: marcos.silva4@arapiraca.ufal.br


## Próximos Passos:

O projeto será expandido com a implementação de outros algoritmos de resolução para o PCV para lidar com conjuntos de dados maiores de forma mais eficiente.


## Licença

Este projeto é licenciado sob a Licença Pública Geral GNU v3.0. Você é livre para modificar e distribuir este software de acordo com os termos da licença. Para obter mais detalhes, consulte o [texto completo da licença](https://www.gnu.org/licenses/gpl-3.0.html). Resumo da GNU GPL v3.0

- Você é livre para executar, modificar e compartilhar o software.
- Quaisquer modificações feitas devem ser liberadas sob a mesma licença durante a distribuição.
- Este software é distribuído sem qualquer garantia; consulte a licença para obter detalhes.

<hr>

**raquel linda ❤️**
