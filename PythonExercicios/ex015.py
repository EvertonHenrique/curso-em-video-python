dias = int(input('Quantos dias o carro foi alugado? '))
rodagem = float(input('Quantos km rodados? '))
pago = (dias * 60) + (rodagem * 0.15)
print(f'O total a pagar é de R${pago:.2f}')