print('-=' * 30)
print('Analisando Triangulos'.center(50))
print('-=' * 30)
t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segundo Segmento: '))
t3 = float(input('Terceiro Segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print(f'TRIÂNGULO FORMADO COM SUCESSO!')
    if t1 == t2 == t3:
        print('EQUILATERO!')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('NÃO PODEMOS FORMAR UM TRIÂNGULO!')