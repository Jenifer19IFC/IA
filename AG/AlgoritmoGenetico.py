import random

class AlgoritmoGenetico:

    def __init__(self, tamanho_populacao, num_horarios, taxa_mutacao, num_geracoes, populacao_inicial):
        self.tamanho_populacao = tamanho_populacao
        self.num_horarios = num_horarios # Quantos horários serão alocados para cada pessoa em cada dia
        self.taxa_mutacao = taxa_mutacao
        self.num_geracoes = num_geracoes
        self.populacao_inicial = populacao_inicial

    # Criação da população inicial
    def cria_populacao(self):
        populacao = []
        for _ in range(self.tamanho_populacao):
            individuo = {}
            for nome in self.populacao_inicial:
                disponibilidade = self.populacao_inicial[nome]
                horario_reuniao = {}
                for dia, horas in disponibilidade.items():
                    num_horarios = min(self.num_horarios, len(horas))
                    # Garantir que não há repetição de horários para o mesmo dia
                    horarios_escolhidos = set()
                    while len(horarios_escolhidos) < num_horarios:
                        horario_escolhido = random.choice(horas)
                        if horario_escolhido in horarios_escolhidos:   # Se o horário já estiver no conjunto, escolha um novo horário
                            continue
                        horarios_escolhidos.add(horario_escolhido)
                    horario_reuniao[dia] = list(horarios_escolhidos)
                individuo[nome] = horario_reuniao
            populacao.append(individuo)
        return populacao

    def calcula_fitness(self, individuo):
        fitness = 0
        sobreposicoes = 0
        for nome, disponibilidade in individuo.items():
            for dia, horas in disponibilidade.items(): # Percorre cada dia e respectivos intervalos de tempo disp. p/ indivíduo atual
                fitness += len(horas)
                for outro_nome, outra_disponibilidade in individuo.items():  # Verifique se há sobreposições
                    if outro_nome != nome:
                        outras_horas = outra_disponibilidade.get(dia, [])
                        sobreposicoes += len(set(horas) & set(outras_horas)) # Interseção entre indivíduo atual e outro (horas)

        # Penaliza a fitness por qualquer sobreposição
        fitness -= sobreposicoes * 2  # Aumenta o fator de penalização
        fitness = max(fitness, 1)  # Evite a divisão por zero
        return fitness

    # Seleção por roleta dos indivíduos para cruzamento
    def selecao_roleta(self, populacao):
        total_fitness = sum(self.calcula_fitness(individuo) for individuo in populacao) # Calcula o fitness total da pop.
        roleta = [self.calcula_fitness(individuo) / total_fitness for individuo in populacao] # Probabilidade de seleção 
        selecionados = random.choices(populacao, weights=roleta, k=len(populacao)) # Selec. indivíduos com base nas probabilidades
        return selecionados

    # Cruzamento entre dois indivíduos
    def cruzamento(self, individuo1, individuo2):
        novo_individuo = {}
        for nome in self.populacao_inicial:
            pai1 = individuo1[nome]
            pai2 = individuo2[nome]
            filho = {}
            
            # Escolhe dois pontos de corte aleatórios
            dias = list(pai1.keys())
            pontos_de_corte = random.sample(dias, 2)
            pontos_de_corte.sort()
            ponto_de_corte1, ponto_de_corte2 = pontos_de_corte
            
            for dia in dias:
                horarios_pai1 = pai1[dia]
                horarios_pai2 = pai2[dia]
                
                # Aplica crossover antes do 1° ponto de corte
                if dia < ponto_de_corte1:
                    novo_horario_pai1 = horarios_pai1 # Herda do pai1
                elif dia == ponto_de_corte1:
                    novo_horario_pai1 = random.sample(horarios_pai1, len(horarios_pai1) // 2)
                else:
                    novo_horario_pai1 = []
                
                # Aplica crossover entre os pontos de corte
                if ponto_de_corte1 < dia < ponto_de_corte2:
                    novo_horario_pai2 = horarios_pai2 # Recombinação de partes do pai 1 com o pai 2
                elif dia == ponto_de_corte2:
                    novo_horario_pai2 = random.sample(horarios_pai2, len(horarios_pai2) // 2)
                else:
                    novo_horario_pai2 = []
                
                # Aplica crossover após o 2° ponto de corte
                if dia > ponto_de_corte2:
                    novo_horario_pai1 = horarios_pai1 # Herda do pai1
                elif dia == ponto_de_corte2:
                    novo_horario_pai1 = random.sample(horarios_pai1, len(horarios_pai1) // 2)
                else:
                    novo_horario_pai1 = []
                
                novo_horario = list(set(novo_horario_pai1 + novo_horario_pai2))
                filho[dia] = novo_horario

            novo_individuo[nome] = filho # Novo filho
        return novo_individuo



    def mutacao(self, individuo):
        novo_individuo = individuo.copy() # Cópia do indivíduo
        for nome in self.populacao_inicial:
            disponibilidade = self.populacao_inicial[nome]
            for dia, horas in disponibilidade.items():
                if random.random() < self.taxa_mutacao: # Gera um número entre 0 e 1
                    num_horarios = min(self.num_horarios, len(horas)) # Define o n° de horários a serem mutados
                    novo_horario = random.sample(horas, num_horarios) # Subconjunto de n° horários entre as horas do dia
                    novo_individuo[nome][dia] = novo_horario
        return novo_individuo

    # Execução geral do algoritmo genético
    def executar(self):
        populacao = self.cria_populacao()  # Criação da população inicial

        for geracao in range(self.num_geracoes):   # Evolução do algoritmo genético
            populacao = self.selecao_roleta(populacao)
            nova_populacao = []
            while len(nova_populacao) < self.tamanho_populacao:
                individuo1, individuo2 = random.sample(populacao, 2) # Seleciona pais aleatoriamente
                filho = self.cruzamento(individuo1, individuo2) # Novo filho
                filho = self.mutacao(filho) # Aplica (ou não a mutação)
                nova_populacao.append(filho)

            populacao = nova_populacao
            melhor_individuo = max(populacao, key=self.calcula_fitness)  # Encontra o melhor indivíduo na geração atual

           # Imprime as informações da geração atual
            print(f"Geração {geracao + 1} :")
            for nome, disponibilidade in melhor_individuo.items():
                print(f'{nome}: {disponibilidade}')
            print("FITNESS:", self.calcula_fitness(melhor_individuo))
            print("\n" + "="*50 + "\n")

 

