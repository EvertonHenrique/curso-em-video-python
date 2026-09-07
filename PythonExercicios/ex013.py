salario = float(input('Qual é o Sálario atual? '))
novo = salario + (salario * 15/100)
print(f'Atualmente o sálario está em R${salario:.2f}')
print(f'E com o reajuste de 15% o salario passa a ser de R${novo:.2f}')