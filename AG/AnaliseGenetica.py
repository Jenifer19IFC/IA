import random  
import matplotlib.pyplot as plt  

class AnaliseGenetica:
    
    def __init__(self, ag):
        self.ag = ag
        self.best_fitness_values = []  # Lista para armazenar os melhores valores de fitness em cada geração

    # Executa o algoritmo genético 
    def executar_algoritmo(self):
        populacao = self.ag.cria_populacao()  # Cria a população inicial

        for geracao in range(self.ag.num_geracoes):  # Itera pelas gerações
            populacao = self.ag.selecao_roleta(populacao)  # Realiza a seleção por roleta
            nova_populacao = []

            while len(nova_populacao) < self.ag.tamanho_populacao:  # Cria nova população para a próxima geração
                individuo1, individuo2 = random.sample(populacao, 2)  # Seleciona dois indivíduos aleatoriamente
                filho = self.ag.cruzamento(individuo1, individuo2)  # Realiza o cruzamento
                filho = self.ag.mutacao(filho)  # Aplica a mutação (ou não) ao indivíduo gerado
                nova_populacao.append(filho)  

            populacao = nova_populacao  # Atualiza a população para a nova geração

            melhor_individuo = max(populacao, key=self.ag.calcula_fitness)  # Encontra o melhor indivíduo
            best_fitness = self.ag.calcula_fitness(melhor_individuo)  # Calcula o fitness 
            self.best_fitness_values.append(best_fitness)  # Add fitness

            print(f"Geração {geracao + 1} :")
            for nome, disponibilidade in melhor_individuo.items():
                print(f'{nome}: {disponibilidade}') 
            print("FITNESS:", best_fitness)  
            print("\n" + "="*50 + "\n")

    # Plota o gráfico da evolução do fitness ao longo das gerações
    def plotar_grafico(self):
        plt.plot(self.best_fitness_values)  
        plt.title('Evolução da Aptidão ao Longo das Gerações')  
        plt.xlabel('Geração')  
        plt.ylabel('Aptidão') 
        plt.show() 
