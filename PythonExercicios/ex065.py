# Resposta do Exercicio 65
r = ''
valor = soma = maior = menor = 0
while r in 'S':
    n = int(input('Digite um numero: '))
    soma += n
    valor += 1
    r = str(input('Quer Continuar [S/N] ? ')).strip().upper()[0]
    if valor == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if r not in 'SsNn':
        print('Dados Invalidos! Tente Novamente!')
        r = str(input('Quer Continuar [S/N] ?')).strip().upper()[0]
media = soma / valor
print('Você digitou {} numeros e a media entre eles foi {:.2f}'.format(valor, media))
print('O maior valor digitado foi {} e o menor valor digitado foi {}.'.format(maior, menor))



