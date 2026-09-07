listagem_precos = ('Lapis', 1.75,
                     'Borracha', 2,
                     'Caderno', 15.90,
                     'Estojo', 25,
                     'Transferidor', 4.20,
                     'Compasso', 9.99,
                     'Mochila', 120.99,
                     'Canetas', 22.30,
                     'Tablet', 725.65,
                     'Livro', )
print('-' * 40)
print('Listagem de Precos'.upper().center(40))
print('-' * 40)
for item in range(0, len(listagem_precos), 2):
    print(f'{listagem_precos[item]:.<40}')
    if item > 1:
        print(f'R${listagem_precos[item]+1}')
