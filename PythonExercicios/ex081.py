numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Ss':
        continue
    else:
        print('ERRO, TENTE NOVAMENTE!')
    if resp in 'Nn':
        break
numeros.sort(reverse=True)
print(f'Ao todo foram digitados {len(numeros)} números')
print(f'Os valores digitados foram {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')