from AlgoritmoGenetico import AlgoritmoGenetico
from AnaliseGenetica import AnaliseGenetica

populacao_inicial = {
    'Ana': {
        'Segunda': [9, 11],
        'Terca': [11, 13],
        'Quarta': [15],
        'Quinta': [10, 12, 13, 14, 15],
        'Sexta': [9, 17]
    },
    'Matheus': {
        'Segunda': [8],
        'Terca': [],
        'Quarta': [9, 10, 12, 14, 15],
        'Quinta': [14],
        'Sexta': []
    },
    'Clara': {
        'Segunda': [9, 10, 11, 13, 15],
        'Terca': [10, 11, 13, 14, 15],
        'Quarta': [9, 11, 12, 14, 15],
        'Quinta': [10, 12, 13, 14, 15],
        'Sexta': [9, 10, 12, 14, 15]
    }
}

ag = AlgoritmoGenetico(tamanho_populacao=50, num_horarios=2, taxa_mutacao=0.5, num_geracoes=100, populacao_inicial=populacao_inicial)

analise = AnaliseGenetica(ag)
analise.executar_algoritmo()
analise.plotar_grafico()