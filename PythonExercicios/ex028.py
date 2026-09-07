from random import randint
from time import sleep
maquina = randint(0, 5) # Faz a Maquina Pensar em um Número entre 0 e 5
print('-=' * 20)
print(' VAMOS PENSAR EM UM NUMERO ENTRE 0 E 5 ')
print('-=' * 20)
jogador = int(input('Em que numero eu PENSEI ? '))
print(' PROCESSANDO... ')
sleep(5)
if jogador == maquina:
    print('PARABENS! Você conseguiu vencer o jogo')
else:
    print('VENCI O JOGO!')