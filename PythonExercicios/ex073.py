times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atletico-MG', 'Botafogo', 'Athletico-PR',
         'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO' )
print('-=' * 30)
print(' LISTA DE TIMES DO BRASILEIRÃO ')
print('-=' * 30)
for p, t in enumerate(times):
    print(f'{p+1}º {t}')
print('-=' * 30)
print(f'Os 5 primeiros colocados, classificados para a Libertadores: {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados rebaixados para a Serie B: {times[-4:]}')
print('-=' * 30)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 30)
print(f'A Chapecoense terminou na {times.index("Chapecoense")+1}ª posição')
print('-=' * 30)