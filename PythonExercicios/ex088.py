from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*40)
print('Sorteador da Mega Sena')
print('-'*40)
quantidade = int(input('Quantos jogos você deseja gerar: '))
tot = 0
while tot <= quantidade:
    contador = 0
    while contador < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*10, f'Sorteando {quantidade} jogos', '-'*10)
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)

