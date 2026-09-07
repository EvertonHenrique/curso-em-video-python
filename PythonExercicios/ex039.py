from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
sexo = str(input('Sexo: '))
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Voce completa {idade} anos esse ano. TEM QUE SE ALISTAR IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'{ano} será o seu ALISTAMENTO!')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já passou do tempo de se Alistar há {saldo} anos!')
    ano = atual - saldo
    print(f'{ano} foi o ano do seu ALISTAMENTO!')

if sexo == 'Ff':
    print('Mulheres não podem se ALISTAR!')