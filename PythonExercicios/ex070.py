# Exercicio 70
print('-=' * 20)
print('LOJA SUPER BARATÃO'.center(40))
print('-=' * 20)
totalCompra = totalMil = menor = cont = 0
barato = ''
while True:
    nomeProduto = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    cont += 1
    totalCompra += preço
    if preço > 1000:
        totalMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nomeProduto
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O Total da Compra foi {totalCompra:.2f}')
print(f'Temos {totalMil} produtos com mais de R$1000,00')
print(f'O produto mais barato foi {barato} e está custando R${menor:.2f}')