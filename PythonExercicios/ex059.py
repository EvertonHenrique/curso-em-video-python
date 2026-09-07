from time import sleep
valor1 = int(input('Primeiro Valor: '))
valor2 = int(input('Segundo Valor: '))
opcão = 0
soma = multiplicação = 0
while opcão != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = valor1 + valor2
        print(f'{valor1} + {valor1} = {soma}')
    elif opção == 2:
        multiplicação = valor1 * valor2
        print(f'{valor1} x {valor2} = {multiplicação}')
    elif opção == 3:
        if valor1 > valor2:
            print('O PRIMEIRO valor é maior')
        elif valor2 > valor1:
            print('O SEGUNDO valor é maior')
    elif opção == 4:
        print('Informe novamente os valores')
        valor1 = int(input('Primeiro Valor: '))
        valor2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('FINALIZANDO.....')
        sleep(1)
        print()
    else:
        print('Dados Invalidos! Tente Novamente!')
print('-='  * 30)
print('FIM DO PROGRAMA!')