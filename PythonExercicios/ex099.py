def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
    cont = len(num)
    if cont > 0:
        mai = max(num)
    else:
        mai = 0
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {mai}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()