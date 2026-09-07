print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)
n = int(input('Digite quantos termos para Sequencia de fibonacci: '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t4 = t1 + t2
    t1 = t2
    t2 = t4
    print(' - {}'.format(t4), end='')
    cont += 1
print(' - FIM!')