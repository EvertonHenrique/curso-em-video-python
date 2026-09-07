import math
print('-+' * 20)
print('10 Termos da Progressão Aritimetica'.center(30))
print('-+' * 20)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimoTermo = termo + (10 - 1) * razao
for c in range(termo, decimoTermo+razao, razao):
    print(f'{c} ', end=' - ')
print('FIM')
