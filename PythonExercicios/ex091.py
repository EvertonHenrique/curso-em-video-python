from random import randint
from operator import itemgetter
from time import sleep
jogador = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('<= Valores sorteados =>')
print('-=' * 20)
for k, v in jogador.items():
    print(f' O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('Ranking dos jogadores')
print('-=' * 20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

