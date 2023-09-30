from collections import deque
import time

class BuscaAestrela:

    def __init__(self, estado_inicial, estado_final, tipo_heuristica):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.tipo_heuristica = tipo_heuristica

    # N° peças fora do lugar
    def heuristica_g(self, estado_atual): 
        count = 0
        for i in range(3):
            for j in range(3):
                if estado_atual[i][j] != self.estado_final[i][j]:
                    count += 1
        return count
    
    # g(x) = número de peças fora do lugar
    # h(x) = número de movimentos para colocar a peça no lugar (Distância de Manhattan)
    def heuristica_h(self, estado_atual):
        total_distancia = 0
        for i in range(3):
            for j in range(3):
                valor = estado_atual[i][j]
                if valor != 0:
                    objetivo_i, objetivo_j = self.encontrar_posicao_valor(self.estado_final, valor)
                    # Distância Manhattan = |x1 - x2| + |y1 - y2|
                    distancia = abs(i - objetivo_i) + abs(j - objetivo_j)
                    total_distancia += distancia
        return total_distancia

    def encontrar_posicao_valor(self, estado, valor):
        for i in range(3):
            for j in range(3):
                if estado[i][j] == valor:
                    return i, j

    def buscar(self):
        abertos = []
        fechados = set()
        caminho = {}
        passo = 0
        tamanho_arvore = 1
        inicio_tempo = time.time()

        estado_inicial_tupla = tuple(map(tuple, self.estado_inicial)) # Imutável
        caminho[estado_inicial_tupla] = None

        if (self.tipo_heuristica == 'G'):
            custo_inicial = self.heuristica_g(self.estado_inicial) 
        else:
             custo_inicial = self.heuristica_g(self.estado_inicial) + self.heuristica_h(self.estado_inicial)


        abertos.append((self.estado_inicial, custo_inicial))

        while abertos:
            abertos.sort(key=lambda x: x[1]) # Ordena os nós abertos pelo custo
            estado_atual, _ = abertos.pop(0) # Pega o nó com menor custo
            estado_atual_tupla = tuple(map(tuple, estado_atual))

            print(f"Iteração {passo + 1}:")
            self.imprimir_matriz(estado_atual)

            if tuple(map(tuple, estado_atual)) == tuple(map(tuple, self.estado_final)):
                fim_tempo = time.time()
                tempo_busca = fim_tempo - inicio_tempo
                print(f"Tempo de busca: {tempo_busca} segundos")
                print(f"Tamanho da árvore de busca: {tamanho_arvore} nós")
                return self.construir_caminho(caminho, estado_atual), tempo_busca, tamanho_arvore

            if estado_atual_tupla in fechados:
                continue

            sucessores = self.gerar_sucessores(list(map(list, estado_atual)))
            for sucessor in sucessores:
                sucessor_tupla = tuple(map(tuple, sucessor))
                if sucessor_tupla not in fechados:
                    if (self.tipo_heuristica == 'G'):
                        custo_sucessor = self.heuristica_g(sucessor) 
                    else:
                        custo_sucessor = self.heuristica_g(sucessor) + self.heuristica_h(sucessor)

                    abertos.append((sucessor, custo_sucessor))
                    caminho[sucessor_tupla] = estado_atual_tupla
                    tamanho_arvore += 1
                    passo += 1
                    print(f"Iteração {passo + 1}:")
                    self.imprimir_matriz(estado_atual)

            fechados.add(estado_atual_tupla)
            if estado_atual in abertos:
                abertos.remove(estado_atual)

            limite_tempo = 60  # Em segundos
            tempo_atual = time.time() - inicio_tempo

            if tempo_atual > limite_tempo:
                print("\nTempo de busca excedeu o limite.")
                return None

        return None

    def gerar_sucessores(self, estado):
        linha, coluna = self.encontrar_posicao_vazia(estado)
        sucessores = []
        movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for movimento in movimentos:
            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]
            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3: # Limites do tabuleiro
                novo_estado = [list(row) for row in estado]
                novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna] # Troca
                sucessores.append(novo_estado)

        return sucessores

    def encontrar_posicao_vazia(self, estado):
        for i in range(3):
            for j in range(3):
                if estado[i][j] == 0:
                    return i, j

    def construir_caminho(self, caminho, estado_final):
        caminho_sol = [estado_final]
        estado_atual = estado_final
        estado_atual = tuple(map(tuple, estado_atual))

        while caminho[estado_atual] is not None:
            estado_atual = caminho[estado_atual]
            caminho_sol.append(estado_atual)

        caminho_sol.reverse()
        return caminho_sol

    def imprimir_matriz(self, matriz):
        for linha in matriz:
            print(' '.join(map(str, linha)))
        print()
