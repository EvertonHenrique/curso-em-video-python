def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')


# Programa Principal
print('-' * 30)
print('CONTROLE DE TERRENOS'.center(30))
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)