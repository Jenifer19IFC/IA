import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Criação das variáveis de entrada 
sexo = ctrl.Antecedent(np.arange(0, 2, 1), 'sexo')
imcM = ctrl.Antecedent(np.arange(0, 40, 1), 'imcM')
imcH = ctrl.Antecedent(np.arange(0, 40, 1), 'imcH')
gordura_corporalM = ctrl.Antecedent(np.arange(0, 40, 1), 'gordura_corporalM')
gordura_corporalH = ctrl.Antecedent(np.arange(0, 40, 1), 'gordura_corporalH')

# Criação da variável de saída
status_fisico = ctrl.Consequent(np.arange(0, 11, 1), 'status_fisico')

# Mapeamento dos valores para SEXO
sexo['mulher'] = fuzz.trimf(sexo.universe, [0, 0, 1])
sexo['homem'] = fuzz.trimf(sexo.universe, [0, 1, 1])

# Definição do IMC para MULHERES
imcM['baixo_peso_mulher'] = fuzz.trimf(imcM.universe, [0, 18, 18])
imcM['peso_adequado_mulher'] = fuzz.trimf(imcM.universe, [18.1, 23.9, 23.9])
imcM['sobrepeso_mulher'] = fuzz.trimf(imcM.universe, [24, 28.9, 28.9])
imcM['obesidade_mulher'] = fuzz.trimf(imcM.universe, [29, 40, 40])

# Definição do IMC para HOMENS
imcH['baixo_peso_homem'] = fuzz.trimf(imcH.universe, [0, 19, 19])
imcH['peso_adequado_homem'] = fuzz.trimf(imcH.universe, [19.1, 24.9, 24.9])
imcH['sobrepeso_homem'] = fuzz.trimf(imcH.universe, [25, 29.9, 29.9])
imcH['obesidade_homem'] = fuzz.trimf(imcH.universe, [30, 40, 40])

# Definição da GORDURA CORPORAL para MULHERES
gordura_corporalM['baixo_gordura_mulher'] = fuzz.trimf(gordura_corporalM.universe, [0, 15, 15])
gordura_corporalM['ideal_gordura_mulher'] = fuzz.trimf(gordura_corporalM.universe, [15.1, 23, 23])
gordura_corporalM['alto_gordura_mulher'] = fuzz.trimf(gordura_corporalM.universe, [23.1, 29, 29])
gordura_corporalM['muito_alto_gordura_mulher'] = fuzz.trimf(gordura_corporalM.universe, [29.1, 40, 40])

# Definição da GORDURA CORPORAL para HOMENS
gordura_corporalH['baixo_gordura_homem'] = fuzz.trimf(gordura_corporalH.universe, [0, 8, 8])
gordura_corporalH['ideal_gordura_homem'] = fuzz.trimf(gordura_corporalH.universe, [8.1, 18, 18])
gordura_corporalH['alto_gordura_homem'] = fuzz.trimf(gordura_corporalH.universe, [18.1, 25, 25])
gordura_corporalH['muito_alto_gordura_homem'] = fuzz.trimf(gordura_corporalH.universe, [25.1, 40, 40])

# Definição das variáveis de SAÍDA
status_fisico['eminencia_magreza'] = fuzz.trimf(status_fisico.universe, [0, 0, 5])
status_fisico['ideal'] = fuzz.trimf(status_fisico.universe, [0, 5, 10])
status_fisico['eminencia_sobrepeso'] = fuzz.trimf(status_fisico.universe, [5, 10, 10])

# Definição das regras
# Mulheres
ruleM1 = ctrl.Rule(sexo['mulher'] & imcM['baixo_peso_mulher'] & gordura_corporalM['baixo_gordura_mulher'], status_fisico['eminencia_magreza'])
ruleM2 = ctrl.Rule(sexo['mulher'] & imcM['baixo_peso_mulher'] & gordura_corporalM['ideal_gordura_mulher'], status_fisico['eminencia_magreza'])
ruleM3 = ctrl.Rule(sexo['mulher'] & imcM['baixo_peso_mulher'] & gordura_corporalM['alto_gordura_mulher'], status_fisico['eminencia_magreza'])
ruleM4 = ctrl.Rule(sexo['mulher'] & imcM['baixo_peso_mulher'] & gordura_corporalM['muito_alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])

ruleM5 = ctrl.Rule(sexo['mulher'] & imcM['peso_adequado_mulher'] & gordura_corporalM['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM6 = ctrl.Rule(sexo['mulher'] & imcM['peso_adequado_mulher'] & gordura_corporalM['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM7 = ctrl.Rule(sexo['mulher'] & imcM['peso_adequado_mulher'] & gordura_corporalM['alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])
ruleM8 = ctrl.Rule(sexo['mulher'] & imcM['peso_adequado_mulher'] & gordura_corporalM['muito_alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])

ruleM9 = ctrl.Rule(sexo['mulher'] & imcM['sobrepeso_mulher'] & gordura_corporalM['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM10 = ctrl.Rule(sexo['mulher'] & imcM['sobrepeso_mulher'] & gordura_corporalM['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM11 = ctrl.Rule(sexo['mulher'] & imcM['sobrepeso_mulher'] & gordura_corporalM['alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])
ruleM12 = ctrl.Rule(sexo['mulher'] & imcM['sobrepeso_mulher'] & gordura_corporalM['muito_alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])

ruleM13 = ctrl.Rule(sexo['mulher'] & imcM['obesidade_mulher'] & gordura_corporalM['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM14 = ctrl.Rule(sexo['mulher'] & imcM['obesidade_mulher'] & gordura_corporalM['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM15 = ctrl.Rule(sexo['mulher'] & imcM['obesidade_mulher'] & gordura_corporalM['alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])
ruleM16 = ctrl.Rule(sexo['mulher'] & imcM['obesidade_mulher'] & gordura_corporalM['muito_alto_gordura_mulher'], status_fisico['eminencia_sobrepeso'])

# Homens
ruleH1 = ctrl.Rule(sexo['homem'] & imcH['baixo_peso_homem'] & gordura_corporalH['baixo_gordura_homem'], status_fisico['eminencia_magreza'])
ruleH2 = ctrl.Rule(sexo['homem'] & imcH['baixo_peso_homem'] & gordura_corporalH['ideal_gordura_homem'], status_fisico['eminencia_magreza'])
ruleH3 = ctrl.Rule(sexo['homem'] & imcH['baixo_peso_homem'] & gordura_corporalH['alto_gordura_homem'], status_fisico['eminencia_magreza'])
ruleH4 = ctrl.Rule(sexo['homem'] & imcH['baixo_peso_homem'] & gordura_corporalH['muito_alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])

ruleH5 = ctrl.Rule(sexo['homem'] & imcH['peso_adequado_homem'] & gordura_corporalH['baixo_gordura_homem'], status_fisico['ideal'])
ruleH6 = ctrl.Rule(sexo['homem'] & imcH['peso_adequado_homem'] & gordura_corporalH['ideal_gordura_homem'], status_fisico['ideal'])
ruleH7 = ctrl.Rule(sexo['homem'] & imcH['peso_adequado_homem'] & gordura_corporalH['alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])
ruleH8 = ctrl.Rule(sexo['homem'] & imcH['peso_adequado_homem'] & gordura_corporalH['muito_alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])

ruleH9 = ctrl.Rule(sexo['homem'] & imcH['sobrepeso_homem'] & gordura_corporalH['baixo_gordura_homem'], status_fisico['ideal'])
ruleH10 = ctrl.Rule(sexo['homem'] & imcH['sobrepeso_homem'] & gordura_corporalH['ideal_gordura_homem'], status_fisico['ideal'])
ruleH11 = ctrl.Rule(sexo['homem'] & imcH['sobrepeso_homem'] & gordura_corporalH['alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])
ruleH12 = ctrl.Rule(sexo['homem'] & imcH['sobrepeso_homem'] & gordura_corporalH['muito_alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])

ruleH13 = ctrl.Rule(sexo['homem'] & imcH['obesidade_homem'] & gordura_corporalH['baixo_gordura_homem'], status_fisico['ideal'])
ruleH14 = ctrl.Rule(sexo['homem'] & imcH['obesidade_homem'] & gordura_corporalH['ideal_gordura_homem'], status_fisico['ideal'])
ruleH15 = ctrl.Rule(sexo['homem'] & imcH['obesidade_homem'] & gordura_corporalH['alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])
ruleH16 = ctrl.Rule(sexo['homem'] & imcH['obesidade_homem'] & gordura_corporalH['muito_alto_gordura_homem'], status_fisico['eminencia_sobrepeso'])


# Criação e simulação do sistema de controle
status_ctrl = ctrl.ControlSystem([ruleM1, ruleM2, ruleM3, ruleM4, ruleM5, ruleM6, ruleM7, ruleM8, ruleM9, ruleM10, ruleM11, ruleM12, ruleM13, ruleM14, ruleM15, ruleM16, ruleH1, ruleH2, ruleH3, ruleH4, ruleH5, ruleH6, ruleH7, ruleH8, ruleH9, ruleH10, ruleH11, ruleH12, ruleH13, ruleH14, ruleH15, ruleH16]) 
status = ctrl.ControlSystemSimulation(status_ctrl)

# Definição de valores de entrada
status.input['sexo'] = 0  # 0 - Mulher | 1 - Homem

status.input['imcM'] = 5
status.input['gordura_corporalM'] =  19

status.input['imcH'] = np.nan
status.input['gordura_corporalH'] = np.nan

# Computa o resultado
status.compute()

# Acessar o valor do centroide da variável de saída
valor_centroide = status.output['status_fisico']
print("Valor do centroide:", valor_centroide)

# Visualização do resultado
print(status.output['status_fisico'])

gordura_corporalM.view() 
imcM.view()

gordura_corporalH.view() 
imcH.view()

sexo.view()
status_fisico.view(sim=status)

# Mostra centróide no gráfico
plt.axvline(x=valor_centroide, color='r', linestyle='--', label='Centroide')
# plt.plot(valor_centroide, 0, 'ro', markersize=10, label='Centroide')
plt.legend()

plt.show() # Permanece aberto

