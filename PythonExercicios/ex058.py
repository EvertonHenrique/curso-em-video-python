from random import randint
from time import sleep
maquina = randint(0, 10) # Faz a Maquina Pensar em um Número entre 0 e 10
print('-=' * 20)
print(' VAMOS PENSAR EM UM NUMERO ENTRE 0 E 10 ')
print('-=' * 20)
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Em que numero eu PENSEI ? '))
    print(' PROCESSANDO... ')
    sleep(5)
    palpites += 1
    if jogador == maquina:
        acerto = True
    else:
        if jogador < maquina:
            print('Mais..... Tente mais uma vez')
        elif jogador > maquina:
            print('Menos..... Tente mais uma vez')
print(F'ACERTOU! com {palpites} tentativas. ')