# Exercicio 67
while True:
    n = int(input('Quer ver a TABUADA de qual valor [NUMERO NEGATIVO INTERROMPE] ? '))
    print('-=' * 30)
    if n < 0:
        break
    for c in range(0, 10):
        c += 1
        print(f'{n} x {c} = {n*c}')
    print('-=' * 30)
print('PROGRAMA DE TABUADA ENCERRADO!')