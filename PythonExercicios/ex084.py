dados = list()
princ = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    princ.append(dados[:])
    dados.clear()
    resp = str(input("Quer Continuar [S/N]? "))
    if resp in 'Nn':
        break
mai = max(princ)
men = min(princ)
print('-' * 30)
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'{mai} foram as pessoas mais pesadas')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'{men} foram as pessoas menos pesadas')
