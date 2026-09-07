distancia = float(input('Qual é a Distância da sua viagem? '))
print(f'Sua  distancia da viagem é de {distancia}KM/h.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da sua passagem ficou em R${preco:.2f}.')