from math import hypot
oposto = float(input('Comprimento do Cateto Oposto: '))
adjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')