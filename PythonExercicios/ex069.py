# Exercicio 69
print('-=' * 20)
print('MINI-CADASTRO DE PESSOAS'.center(40))
print('-=' * 20)
total18 = 0
mulheresDe20 = 0
homens = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo not in 'MF':
        print('ERRO! Digite Novamente seu Sexo! ')
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresDe20 += 1
    resposta = str(input('Quer Continuar? [S/N] ? ')).strip().upper()[0]
    if resposta not in 'SN':
        print('ERRO! Digite Novamente! ')
        resposta = str(input('Quer Continuar? [S/N] ? ')).strip().upper()[0]
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
print(f'O total de pessoas com mais de 18 anos foram {total18} pessoas.')
print(f'Temos um total de {homens} homens cadastrados')
print(f'Ao todo temos {mulheresDe20} mulheres com menos de 20 Anos.')