from datetime import datetime
atual = datetime.now().year
maiorIdade = 0
menorIdade = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Ano de Nascimento: {pessoa}ª Pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'{maiorIdade} pessoas maiores de idade \n{menorIdade} pessoas menores de Idade ')