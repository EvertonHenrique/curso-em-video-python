import math
print('-+' * 20)
print('Termos da Progressão Aritimetica'.center(30))
print('-+' * 20)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
t = termo
c = 1
while c <= 10:
    print(f'{t} - ', end='')
    t += razao
    c += 1

