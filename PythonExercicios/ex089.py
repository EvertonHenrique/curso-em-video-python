dados = list()
from time import sleep
while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-='*30)
while True:
    opcao = int(input('Mostrar dados de qual aluno? (999 encerra) '))
    if opcao == 999:
        print('Finalizando...')
        sleep(1)
        break

    if opcao <= len(dados) - 1:
        print(f'Notas de {dados[opcao][0]} são {dados[opcao][1]}')
print('<= Programa Finalizado =>  <= Volte Sempre =>')
