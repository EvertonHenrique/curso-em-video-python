from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores passados: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[c]} ', end='', flush=True)
        sleep(0.2)
    print('PRONTO!')



def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia(numeros)
somaPar(numeros)