sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção Invalida! Tente Novamente! Digite seu sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Opção Invalida! Tente Novamente!')
print('Sexo {} registrado com sucesso! '.format(sexo))