numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Lista Completa: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')