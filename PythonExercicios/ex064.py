

num = soma = quantidade = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma += num
        quantidade += 1
print('A soma entre os numeros é {} e a quantidade de numeros digitados é {}'.format(soma, quantidade))



# Resposta do Exercicio 64
'''num = soma = quantidade = 0
while num != 999:
    num = int(input('Digite um numero: [999 para parar] '))
    soma += num
    quantidade += 1
print('A soma entre os numeros é {} e a quantidade é {}'.format(soma - 999, quantidade - 1))'''''
