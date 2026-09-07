largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
área = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {área}m2')
tinta = área / 2
print(f'Para pintar uma parede, voce precisará de {tinta}l de tinta')
