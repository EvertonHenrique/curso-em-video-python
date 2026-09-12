def ficha(jogador, gols):
     print(f'O jogador {jogador} fez {gols} gols')
# Programa Principal
j = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)