salario = float(input('Qual é o salário do Funcionario: '))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100 )
else:
    novoSalario = salario + (salario * 10 / 100)
print(f'O Salario do funcionario foi de R${salario} para R${novoSalario:.2f} ')