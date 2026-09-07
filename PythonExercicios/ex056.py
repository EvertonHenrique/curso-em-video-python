somaIdade = 0
media = 0
maioridadeMasc = 0
mulherDe20 = 0
nomeHomemVelho = ''
for p in range(1, 5):
    print(f'----------- {p}ª PESSOA ----------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeMasc = idade
        nomeHomemVelho = nome
    if sexo in 'Mm' and idade > maioridadeMasc:
        maioridadeMasc = idade
        nomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherDe20 += 1
media = somaIdade / 4
print(f'A média da idade do grupo é de {media}')
print(f'{nomeHomemVelho} é o homem mais velho do grupo ')
print(f'Temos {mulherDe20} mulheres com menos de 20 anos')