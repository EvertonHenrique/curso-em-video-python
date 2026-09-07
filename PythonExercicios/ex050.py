soma = 0
cont = 0
for n in range(1, 7):
    n = int(input(f'Digite um Valor: '))
    if n % 2 == 0:
        soma += n
        cont +=1
print(f'foram informados {cont} numeros pares e a soma foi {soma}')