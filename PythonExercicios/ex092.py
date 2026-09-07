from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
ano = date.today().year
dados['idade'] = ano - nascimento
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    if dados['idade'] < 65:
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano)

print('-=' * 25)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
print('-=' * 25)