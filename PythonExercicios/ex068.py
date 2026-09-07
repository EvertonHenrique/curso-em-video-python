# Exercicio 68
from random import randint
print('-=' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 15)
vitorias = 0
while True:
    jogador = int(input('Diga um Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    if tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Joguei {jogador} e o Computador {computador}')
    print('DEU PAR! ' if total % 2 == 0 else f'DEU IMPAR! Total de {total} jogadas ', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU! ')
            vitorias += 1
        else:
            print('VOCÊ PERDEU! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
print(f'GAME OVER! Você teve {vitorias} Vitorias')
