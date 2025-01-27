'''
Desafio 1: Crie um programa em Python que:

Solicite ao usuário uma lista de números (separados por vírgula).
Calcule e exiba as seguintes medidas estatísticas:
- Média
- Mediana
- Moda
- Variância
- Desvio padrão
- Amplitude
'''

import numpy as np
import pandas as pd

print('='*140)
print('Cálculo de Estatística Descritiva')
print('='*140)

print('\nDigite uma lista de número separado por vírgulas para o cálculo de Estatística Descritiva')

while True:
    try:
        entrada = (input('\nDigite uma lista de números separados por vírgula: '))
        dados = [float(x.strip()) for x in entrada.split(',')]
        break
    except ValueError:
        print('Erro! Por favor, certifique-se de inserir números separados por vírgula corretamente.')


# Imprimindo os dados para o usuário ver
print(f'\nA sua lista de números é: {dados}')


# Média
media = np.mean(dados)

# Mediana
mediana = np.median(dados)

# Variância
variancia = np.var(dados)

# Desvio Padrão
desvio_padrao = np.std(dados)

# Amplitude
amplitude = np.max(dados) - np.min(dados)

# Tratamento de Erro para o cálculo da Moda
try:
    moda = pd.Series(dados).mode().tolist()
    moda_str = ', '.join(str(m) for m in moda)
except:
    moda_str = "Nenhuma moda encontrada (valores únicos)."

# Exibindo os resultados
print('-'*140)
print(f'Média: {media:.2f}')
print(f'\nMediana: {mediana:.2f}')
print(f'\nModa: {moda}')
print(f'\nVariância: {variancia:.2f}')
print(f'\nDesvio Padrão: {desvio_padrao:.2f}')
print(f'\nAmplitude: {amplitude}\n\n')