from math import pow
peso = float(input('Qual é o seu Peso (em KG)? '))
altura = float(input('Qual é a sua Altura (em m)? '))
imc = peso / pow(altura, 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MORBIDA')