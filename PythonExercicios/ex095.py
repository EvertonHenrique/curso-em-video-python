futebol = dict()
time = list()
partidas = list()
from time import sleep
while True:
    futebol.clear()
    futebol['jogador'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
    n = 0
    partidas.clear()
    while n < tot:
        partidas.append(int(input(f'Quantos gols na partida {n}? ')))
        n += 1
    futebol['gols'] = partidas[:]
    futebol['total'] = sum(partidas)
    time.append(futebol.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
# Cabeçalho da tabela
print(f'{"cod":<5}{"nome":<16}{"gols":<16}{"total":<6}')
print('-' * 40)

# Linhas com os dados dos jogadores
for k, v in enumerate(time):
    print(f'{k:<5}{v["jogador"]:<16}{str(v["gols"]):<16}{v["total"]:<6}')
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar): ? '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO: Não existe jogador com codigo {}'.format(busca))
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}: ')
        for a, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {a+1} fez {g} gols.')
            sleep(1)
print('-' * 40)
print('FIM DO PROGRAMA')
print('-' * 40)
