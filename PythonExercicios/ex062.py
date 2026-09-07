import math
print('-+' * 20)
print('Termos da Progressão Aritimetica'.center(30))
print('-+' * 20)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
n = 10
c = 1
total = 0
while n != 0:
    total += n
    t = termo
    while c <= 10:
        print(f'{t} - ', end='')
        t += razao
        c += 1
    print('PAUSA')
    n = int(input('Quer mostrar quantos termos a mais? '))
print(f'Progressão Finalizada com sucesso. São {total} termos a mais')