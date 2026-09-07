casa = float(input('Valor da Casa: R$'))
salario = float(input('Salario do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa /(anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos}', end="")
print(f' a prestação é de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo Concedido!')
else:
    print('Emprestimo Negado!')