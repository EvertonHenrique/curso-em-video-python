n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[35m{c} ', end=' ')
        total += 1
    else:
        print(f'\033[32m{c} ', end=' ')
print('\033[m')
print(f'O numero {n} foi divisivel {total} vezes.')
if total == 2:
    print('E por isso ele é um NUMERO PRIMO')
else:
    print('E por isso ele NÃO é um NUMERO PRIMO')