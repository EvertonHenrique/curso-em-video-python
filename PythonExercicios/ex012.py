preço = float(input('Qual o preço do produto? '))
novoPreço = preço - (preço * 5 / 100)
print(f'O produto custava R${preço}')
print(f'Na Promoção de 5% custa R${novoPreço:.2f}.')