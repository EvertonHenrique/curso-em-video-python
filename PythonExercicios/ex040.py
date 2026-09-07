nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando as notas {nota1} e {nota2} a media é {medi}')
if media >= 7:
    print('Aluno APROVADO!')
elif media < 5:
    print('Aluno REPROVADO!')
else:
    print('Aluno em RECUPERAÇÃO')