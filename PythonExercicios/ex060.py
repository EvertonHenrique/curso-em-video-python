'''from math import factorial
n = int(input('Fatorial: '))
f = factorial(n)
print(f'o Fatorial de {n} é {f}')'''

n = int(input('Digite um numero para calcular o Fatorial: '))
f = n
t = 1
print(f'Calculando {f}! ')
while f > 0:
    print(f'{f}', end='')
    if f > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    t *= f
    f -= 1
print(f'{t}')