# Exercicio 71 (O mais dificil do Curso)
print('-=' * 30)
print('BANCO CEV'.center(60))
print('-=' * 30)
cedulas = int(input('Qual valor você quer sacar? R$'))
cinquenta = 50
vinte = 20
dez = 10
um = 1
totalCedulas = 0
cedAtual = 0
while True:
    if cedulas >= cinquenta:
        cedulas -= cinquenta
    elif cedulas >= vinte:
        cedulas -= vinte
    elif cedulas >= dez:
        cedulas -= dez

    else:
        cedAtual = cinquenta
        if totalCedulas > 0:
            print('-=' * 30)
            print(f'{totalCedulas} Cedulas de R${cinquenta}')
            print(f'{totalCedulas} Cedulas de R${vinte}')
            print(f'{totalCedulas} Cedulas de R${dez}')
            print(f'{totalCedulas} Cedulas de R${um}')
        totalCedulas = 0
        if cedulas == 0:
            break

