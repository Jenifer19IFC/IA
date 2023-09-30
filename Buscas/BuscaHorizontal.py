import random
import time

class BuscaHorizontal:

    def __init__(self, estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.limite_iteracoes_sem_sucesso = 3000  

    def buscar(self):
        abertos = []
        fechados = set()
        caminho = {}
        passo = 0
        tamanho_arvore = 1
        inicio_tempo = time.time()
        iteracoes_sem_sucesso = 0  

        estado_inicial_tupla = tuple(map(tuple, self.estado_inicial))
        caminho[estado_inicial_tupla] = None

        abertos.append(estado_inicial_tupla)
        encontrou_sucesso = False 
        
        while abertos:
            estado_atual = abertos.pop(0)

            print(f"Iteração {passo + 1}:")
            self.imprimir_matriz(estado_atual)
           
            if tuple(map(tuple, estado_atual)) == tuple(map(tuple, self.estado_final)):
                fim_tempo = time.time()
                tempo_busca = fim_tempo - inicio_tempo
                print(f"Tempo de busca: {tempo_busca} segundos")
                print(f"Tamanho da árvore de busca: {tamanho_arvore} nós")
                return self.construir_caminho(caminho, estado_atual), tempo_busca, tamanho_arvore

            if estado_atual in fechados:
                continue

            sucessores = self.gerar_sucessores(estado_atual)
            for sucessor in sucessores:
                if sucessor not in fechados and sucessor not in abertos:
                    abertos.append(sucessor)
                    caminho[sucessor] = estado_atual
                    tamanho_arvore += 1
                    passo += 1

            if not encontrou_sucesso:
                iteracoes_sem_sucesso += 1
                if iteracoes_sem_sucesso == self.limite_iteracoes_sem_sucesso:
                    random.shuffle(abertos)  # Embaralha a lista de abertos
                    print('Embaralhando a lista de abertos...')
                    iteracoes_sem_sucesso = 0 

            fechados.add(estado_atual)
            if estado_atual in abertos:
                abertos.remove(estado_atual)
            
            limite_tempo = 60  # Em segundos
            tempo_atual = time.time() - inicio_tempo

            if tempo_atual > limite_tempo:
                print(f"\nTempo de busca excedeu o limite. \nTempo decorrido: {tempo_atual}")
                return None

        return None

    def gerar_sucessores(self, estado):
        linha, coluna = self.encontrar_posicao_vazia(estado)
        sucessores = []
        movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for movimento in movimentos:
            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]
            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
                novo_estado = [list(row) for row in estado]
                novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
                sucessores.append(tuple(map(tuple, novo_estado)))

        return sucessores

    def encontrar_posicao_vazia(self, estado):
        for i in range(3):
            for j in range(3):
                if estado[i][j] == 0:
                    return i, j

    def construir_caminho(self, caminho, estado_final):
        caminho_sol = [estado_final]
        estado_atual = estado_final

        while caminho[estado_atual] is not None:
            estado_atual = caminho[estado_atual]
            caminho_sol.append(estado_atual)

        caminho_sol.reverse()
        return caminho_sol
   
    def imprimir_matriz(self, matriz):
        for linha in matriz:
            print(' '.join(map(str, linha)))
        print()


