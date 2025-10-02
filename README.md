# Algoritmo de Dijkstra - Busca de Custo Uniforme

Este projeto é uma implementação em Python do algoritmo de Dijkstra para encontrar o caminho de menor custo entre dois vértices em um grafo ponderado. O programa foi desenvolvido como parte de uma atividade acadêmica, focando em robustez, clareza e interatividade.

## Estrutura do Projeto

O repositório está organizado da seguinte forma:


├── README.md         <-- Descrição do projeto

└── src/              <-- Pasta com o código-fonte

├── dijkstra.py   <-- Implementação do algoritmo

└── grafo.json    <-- Grafo de exemplo em formato JSON

## Funcionalidades

- **Leitura de Grafo:** Carrega a estrutura do grafo a partir de um arquivo `JSON`.
- **Algoritmo Eficiente:** Utiliza uma fila de prioridade (`heapq`) para otimizar a busca pelo nó de menor distância.
- **Interface Interativa:** Permite que o usuário insira os vértices de origem e destino e teste múltiplos caminhos sem reiniciar o programa.
- **Tratamento de Erros:** Valida a existência do arquivo, o formato JSON e os vértices informados pelo usuário.
- **Resultados Detalhados:** Exibe o caminho mais curto, o custo total e um detalhamento passo a passo dos custos de cada aresta no caminho.

## Como Executar

1.  **Pré-requisitos:** É necessário ter o Python 3 instalado.

2.  **Baixe os arquivos:**
    * Clique no botão verde `<> Code` no topo desta página.
    * Selecione `Download ZIP`.
    * Extraia os arquivos no seu computador.

3.  **Execute o Script:**
    Abra um terminal ou prompt de comando, navegue até a pasta do projeto e execute:
    ```bash
    python src/dijkstra.py
    ```

4.  **Siga as Instruções:**
    O programa solicitará que você digite os vértices de origem e destino. Os vértices disponíveis (baseado no `grafo.json`) são: A, B, C, D, E, F.

## Autor

* **Victor C. Martins** - [VictorCMartins](https://github.com/VictorCMartins)
