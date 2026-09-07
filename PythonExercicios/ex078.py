listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a {c+1}ª Posição: ')))
print('-' * 40)
mai = max(listanum)
men = min(listanum)
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor da lista foi {mai} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor da lista foi {men} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
