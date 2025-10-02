import json
import heapq

def carregar_grafo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding='utf-8') as f:
            grafo = json.load(f)
        return grafo
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: Formato JSON inválido.")
        return None

def dijkstra(grafo, origem, destino):
    if origem not in grafo:
        print(f"Erro: Vértice de origem '{origem}' não existe no grafo.")
        return None, float('inf')
    if destino not in grafo:
        print(f"Erro: Vértice de destino '{destino}' não existe no grafo.")
        return None, float('inf')
    
    distancias = {no: float('inf') for no in grafo}
    predecessores = {no: None for no in grafo}
    visitados = set()
    
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]  # (distância, nó)
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if no_atual in visitados:
            continue
            
        visitados.add(no_atual)
        
        if no_atual == destino:
            break
        
        for vizinho, peso in grafo[no_atual].items():
            if vizinho not in grafo:
                print(f"Aviso: Vértice '{vizinho}' referenciado mas não definido no grafo.")
                continue
                
            nova_distancia = dist_atual + peso
            
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    
    if distancias[destino] == float('inf'):
        print(f"Não existe caminho de '{origem}' para '{destino}'")
        return None, float('inf')
    
    caminho = []
    no_atual = destino
    
    while no_atual is not None:
        caminho.insert(0, no_atual)
        no_atual = predecessores[no_atual]
    
    return caminho, distancias[destino]

def executar_teste(grafo, origem, destino):
    print(f"\n--- Teste: {origem} → {destino} ---")
    
    caminho, custo_total = dijkstra(grafo, origem, destino)
    
    if caminho:
        print(f"Melhor caminho: {' → '.join(caminho)}")
        print(f"Custo total: {custo_total}")
        
        print("Detalhamento:")
        custo_acumulado = 0
        for i in range(len(caminho) - 1):
            peso = grafo[caminho[i]][caminho[i+1]]
            custo_acumulado += peso
            print(f"  {caminho[i]} → {caminho[i+1]}: {peso} (acumulado: {custo_acumulado})")
    else:
        print("Nenhum caminho encontrado.")
    
    print("-" * 40)

def main():
    print("=== Algoritmo de Dijkstra - Busca com Custo Uniforme ===")
    
    arquivo_grafo = "grafo.json"
    grafo = carregar_grafo(arquivo_grafo)
    
    if grafo is None:
        return
    
    print(f"Grafo carregado com sucesso de '{arquivo_grafo}'")
    print(f"Vértices disponíveis: {', '.join(grafo.keys())}")
    
    while True:
        print("\nDigite os vértices de origem e destino:")
        origem = input("Vértice de origem: ").strip().upper()
        destino = input("Vértice de destino: ").strip().upper()
        
        if origem and destino:
            executar_teste(grafo, origem, destino)
        else:
            print("Entrada inválida. Tente novamente.")
        
        continuar = input("\nDeseja testar outro caminho? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()