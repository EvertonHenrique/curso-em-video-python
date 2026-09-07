nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media:.2f}.')
if media >= 6:
    print(f'Você foi APROVADO! ')
else:
    print(f'Você precisa melhorar seu desempenho!')