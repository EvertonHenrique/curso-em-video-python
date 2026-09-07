numero = [[], []]
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        numero[0].append(n)
    else:
        numero[1].append(n)
numero[0].sort()
numero[1].sort()
print('Os numeros PARES digitados foram: {}'.format(numero[0]))
print('Os numeros IMPARES digitados foram: {}'.format(numero[1]))