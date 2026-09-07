aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] < 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Em Recuperacao'
for k, v in aluno.items():
    print(f'{k}: {v}')
