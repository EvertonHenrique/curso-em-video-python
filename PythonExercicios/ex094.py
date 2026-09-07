dados = dict()
galera = list()
soma = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    dados.clear()
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo tem {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'( {p["nome"]} )', end=' ')
print()
print(f'D) As pessoas que estão acima da média são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('FIM DO PROGRAMA')
print('-=' * 30)
