from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 25)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        for c in range(i, f+1, p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)