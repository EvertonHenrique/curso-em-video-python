from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input('Qual a sua JOGADA? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('''Suas Opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-+' * 10)
if computador == 0: # o COMPUTADOR jogou PEDRA
    if jogador == 0: # o JOGADOR JOGOU PEDRA
        print('DEU EMPATE')
    elif jogador == 1:
        print('Vitória do JOGADOR')
    elif jogador == 2:
        print('Vitória do COMPUTADOR')
    else:
        print('Jogada INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('Vitória do COMPUTADOR')
    elif jogador == 1:
        print('DEU EMPATE')
    elif jogador == 2:
        print('Vitória do JOGADOR')
    else:
        print('Jogada INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('Vitória do JOGADOR')
    elif jogador == 1:
        print('Vitória do COMPUTADOR')
    elif jogador == 2:
        print('DEU EMPATE')
    else:
        print('Jogada INVALIDA!')
