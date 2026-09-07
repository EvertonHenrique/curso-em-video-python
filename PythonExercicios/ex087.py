matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print('-=' * 25)
print(f'A soma dos valores pares é {somaPar}')
mai = max(matriz[1][0], matriz[1][1], matriz[1][2])
somaTerceiraColuna = sum(coluna[2] for coluna in matriz)
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {mai}')
