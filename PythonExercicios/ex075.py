from itertools import count

núm = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último numero: ')))
print(f'Você digitou os valores {núm}')
if 9 in núm:
    print(f'O valor 9 apareceu {núm.count(9)} vezes')
else:
    print('O valor 9 não aparece na tupla.')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª Posição.')
else:
    print('O valor 3 não aparece na tupla')
print('Os valores pares digitados foram ', end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')



