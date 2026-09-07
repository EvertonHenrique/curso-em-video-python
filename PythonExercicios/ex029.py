velocidade = float(input('Quantos KMs seu carro rodou ? '))
if velocidade > 80:
    print('Infelizmente você excedeu o limite de 80KM/h! ')
    multa = (velocidade-80) * 7
    print(f'Você foi multado em R${multa:.2f}')
print('Tenha um bom dia, Dirija com Segurança! ')