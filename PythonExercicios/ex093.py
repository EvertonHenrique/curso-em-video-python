futebol = dict()
partidas = list()
futebol['jogador'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
n = 0
while n < tot:
    partidas.append(int(input(f'Quantos gols na partida {n}? ')))
    n += 1
futebol['gols'] = partidas[:]
futebol['total'] = sum(partidas)
print('-=' * 30)
print(futebol)
print('-=' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {futebol["jogador"]} jogou {len(partidas)} partidas.')
for i, v in enumerate(futebol['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')
