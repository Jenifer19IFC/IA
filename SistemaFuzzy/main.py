import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Criação das variáveis de entrada 
sexo = ctrl.Antecedent(np.arange(0, 2, 1), 'sexo')
imc = ctrl.Antecedent(np.arange(0, 40, 1), 'imc')
gordura_corporal = ctrl.Antecedent(np.arange(0, 40, 1), 'gordura_corporal')
# Criação da variável de saída
status_fisico = ctrl.Consequent(np.arange(0, 11, 1), 'status_fisico')

# Mapeamento dos valores para SEXO
sexo['mulher'] = fuzz.trimf(sexo.universe, [0, 0, 1])
sexo['homem'] = fuzz.trimf(sexo.universe, [0, 1, 1])

# Definição do IMC para MULHERES
imc['baixo_peso_mulher'] = fuzz.trimf(imc.universe, [0, 18, 18])
imc['peso_adequado_mulher'] = fuzz.trimf(imc.universe, [18.1, 23.9, 23.9])
imc['sobrepeso_mulher'] = fuzz.trimf(imc.universe, [24, 28.9, 28.9])
imc['obesidade_mulher'] = fuzz.trimf(imc.universe, [29, 40, 40])

# Definição do IMC para HOMENS
imc['baixo_peso_homem'] = fuzz.trimf(imc.universe, [0, 19, 19])
imc['peso_adequado_homem'] = fuzz.trimf(imc.universe, [19.1, 24.9, 24.9])
imc['sobrepeso_homem'] = fuzz.trimf(imc.universe, [25, 29.9, 29.9])
imc['obesidade_homem'] = fuzz.trimf(imc.universe, [30, 40, 40])

# Definição da GORDURA CORPORAL para MULHERES
gordura_corporal['baixo_gordura_mulher'] = fuzz.trimf(gordura_corporal.universe, [0, 15, 15])
gordura_corporal['ideal_gordura_mulher'] = fuzz.trimf(gordura_corporal.universe, [15.1, 23, 23])
gordura_corporal['alto_gordura_mulher'] = fuzz.trimf(gordura_corporal.universe, [23.1, 29, 29])
gordura_corporal['muito_alto_gordura_mulher'] = fuzz.trimf(gordura_corporal.universe, [29.1, 40, 40])

# Definição da GORDURA CORPORAL para HOMENS
gordura_corporal['baixo_gordura_homem'] = fuzz.trimf(gordura_corporal.universe, [0, 8, 8])
gordura_corporal['ideal_gordura_homem'] = fuzz.trimf(gordura_corporal.universe, [8.1, 18, 18])
gordura_corporal['alto_gordura_homem'] = fuzz.trimf(gordura_corporal.universe, [18.1, 25, 25])
gordura_corporal['muito_alto_gordura_homem'] = fuzz.trimf(gordura_corporal.universe, [25.1, 40, 40])

# Definição das variáveis de SAÍDA
status_fisico['razoavel'] = fuzz.trimf(status_fisico.universe, [0, 0, 5])
status_fisico['ideal'] = fuzz.trimf(status_fisico.universe, [0, 5, 10])
status_fisico['fora_de_forma'] = fuzz.trimf(status_fisico.universe, [5, 10, 10])

# Definição das regras
# Mulheres
ruleM1 = ctrl.Rule(sexo['mulher'] & imc['baixo_peso_mulher'] & gordura_corporal['baixo_gordura_mulher'], status_fisico['razoavel'])
ruleM2 = ctrl.Rule(sexo['mulher'] & imc['baixo_peso_mulher'] & gordura_corporal['ideal_gordura_mulher'], status_fisico['razoavel'])
ruleM3 = ctrl.Rule(sexo['mulher'] & imc['baixo_peso_mulher'] & gordura_corporal['alto_gordura_mulher'], status_fisico['razoavel'])
ruleM4 = ctrl.Rule(sexo['mulher'] & imc['baixo_peso_mulher'] & gordura_corporal['muito_alto_gordura_mulher'], status_fisico['fora_de_forma'])

ruleM5 = ctrl.Rule(sexo['mulher'] & imc['peso_adequado_mulher'] & gordura_corporal['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM6 = ctrl.Rule(sexo['mulher'] & imc['peso_adequado_mulher'] & gordura_corporal['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM7 = ctrl.Rule(sexo['mulher'] & imc['peso_adequado_mulher'] & gordura_corporal['alto_gordura_mulher'], status_fisico['fora_de_forma'])
ruleM8 = ctrl.Rule(sexo['mulher'] & imc['peso_adequado_mulher'] & gordura_corporal['muito_alto_gordura_mulher'], status_fisico['fora_de_forma'])

ruleM9 = ctrl.Rule(sexo['mulher'] & imc['sobrepeso_mulher'] & gordura_corporal['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM10 = ctrl.Rule(sexo['mulher'] & imc['sobrepeso_mulher'] & gordura_corporal['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM11 = ctrl.Rule(sexo['mulher'] & imc['sobrepeso_mulher'] & gordura_corporal['alto_gordura_mulher'], status_fisico['fora_de_forma'])
ruleM12 = ctrl.Rule(sexo['mulher'] & imc['sobrepeso_mulher'] & gordura_corporal['muito_alto_gordura_mulher'], status_fisico['fora_de_forma'])

ruleM13 = ctrl.Rule(sexo['mulher'] & imc['obesidade_mulher'] & gordura_corporal['baixo_gordura_mulher'], status_fisico['ideal'])
ruleM14 = ctrl.Rule(sexo['mulher'] & imc['obesidade_mulher'] & gordura_corporal['ideal_gordura_mulher'], status_fisico['ideal'])
ruleM15 = ctrl.Rule(sexo['mulher'] & imc['obesidade_mulher'] & gordura_corporal['alto_gordura_mulher'], status_fisico['fora_de_forma'])
ruleM16 = ctrl.Rule(sexo['mulher'] & imc['obesidade_mulher'] & gordura_corporal['muito_alto_gordura_mulher'], status_fisico['fora_de_forma'])

# Homens
ruleH1 = ctrl.Rule(sexo['homem'] & imc['baixo_peso_homem'] & gordura_corporal['baixo_gordura_homem'], status_fisico['razoavel'])
ruleH2 = ctrl.Rule(sexo['homem'] & imc['baixo_peso_homem'] & gordura_corporal['ideal_gordura_homem'], status_fisico['razoavel'])
ruleH3 = ctrl.Rule(sexo['homem'] & imc['baixo_peso_homem'] & gordura_corporal['alto_gordura_homem'], status_fisico['razoavel'])
ruleH4 = ctrl.Rule(sexo['homem'] & imc['baixo_peso_homem'] & gordura_corporal['muito_alto_gordura_homem'], status_fisico['fora_de_forma'])

ruleH5 = ctrl.Rule(sexo['homem'] & imc['peso_adequado_homem'] & gordura_corporal['baixo_gordura_homem'], status_fisico['ideal'])
ruleH6 = ctrl.Rule(sexo['homem'] & imc['peso_adequado_homem'] & gordura_corporal['ideal_gordura_homem'], status_fisico['ideal'])
ruleH7 = ctrl.Rule(sexo['homem'] & imc['peso_adequado_homem'] & gordura_corporal['alto_gordura_homem'], status_fisico['fora_de_forma'])
ruleH8 = ctrl.Rule(sexo['homem'] & imc['peso_adequado_homem'] & gordura_corporal['muito_alto_gordura_homem'], status_fisico['fora_de_forma'])

ruleH9 = ctrl.Rule(sexo['homem'] & imc['sobrepeso_homem'] & gordura_corporal['baixo_gordura_homem'], status_fisico['ideal'])
ruleH10 = ctrl.Rule(sexo['homem'] & imc['sobrepeso_homem'] & gordura_corporal['ideal_gordura_homem'], status_fisico['ideal'])
ruleH11 = ctrl.Rule(sexo['homem'] & imc['sobrepeso_homem'] & gordura_corporal['alto_gordura_homem'], status_fisico['fora_de_forma'])
ruleH12 = ctrl.Rule(sexo['homem'] & imc['sobrepeso_homem'] & gordura_corporal['muito_alto_gordura_homem'], status_fisico['fora_de_forma'])

ruleH13 = ctrl.Rule(sexo['homem'] & imc['obesidade_homem'] & gordura_corporal['baixo_gordura_homem'], status_fisico['ideal'])
ruleH14 = ctrl.Rule(sexo['homem'] & imc['obesidade_homem'] & gordura_corporal['ideal_gordura_homem'], status_fisico['ideal'])
ruleH15 = ctrl.Rule(sexo['homem'] & imc['obesidade_homem'] & gordura_corporal['alto_gordura_homem'], status_fisico['fora_de_forma'])
ruleH16 = ctrl.Rule(sexo['homem'] & imc['obesidade_homem'] & gordura_corporal['muito_alto_gordura_homem'], status_fisico['fora_de_forma'])


# Criação e simulação do sistema de controle
status_ctrl = ctrl.ControlSystem([ruleM1, ruleM2, ruleM3, ruleM4, ruleM5, ruleM6, ruleM7, ruleM8, ruleM9, ruleM10, ruleM11, ruleM12, ruleM13, ruleM14, ruleM15, ruleM16, ruleH1, ruleH2, ruleH3, ruleH4, ruleH5, ruleH6, ruleH7, ruleH8, ruleH9, ruleH10, ruleH11, ruleH12, ruleH13, ruleH14, ruleH15, ruleH16]) 
status = ctrl.ControlSystemSimulation(status_ctrl)

# Definição de valores de entrada
status.input['sexo'] = 0  # 0 - Mulher | 1 - Homem
status.input['imc'] = 24.42 
status.input['gordura_corporal'] = 23  

# Computa o resultado
status.compute()

# Visualização do resultado
print(status.output['status_fisico'])
status_fisico.view(sim=status)

plt.show() # Permanece aberto

# sexo.view()
# imc.view()
# gordura_corporal.view()
# plt.show()
