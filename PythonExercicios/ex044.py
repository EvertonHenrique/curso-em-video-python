print('-+-' * 20)
print('Lojas Guanabara'.center(60))
print('-+-' * 20)
preco = float(input('Preço das Compras: R$ '))
print('''
    FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro / PIX / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcoes = int(input('OPÇÃO? '))
if opcoes == 1:
    total = preco - (preco * 10 / 100)
elif opcoes == 2:
    total = preco - (preco * 5 / 100)
elif opcoes == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela}')
elif opcoes == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input('Quantas Parcelas: '))
    parcela = total / totalParcelas
    print(f'Sua Compra será em {totalParcelas}x de {parcela}')
else:
    total = 0
    print('ERRO, TENTE NOVAMENTE!')
print(f'Sua Compra de R${preco} vai custar R${total}')

