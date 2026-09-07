num = int(input('Informe um número: '))
n = f'{num:0>4}'
print(f'Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')