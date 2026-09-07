valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Valor duplicado! Não irei adicionar')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
    print('Opção Invalida! Tente Novamente')
print(f'Você digitou os valores {valores} ')