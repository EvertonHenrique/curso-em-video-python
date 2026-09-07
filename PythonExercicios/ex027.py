n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
ultimo = nome[len(nome)-1]
print(f'Muito prazer em conhece-lo!, {n}!')
print(f'Seu 1º nome é {nome[0]}')
print(f'Seu ultimo nome é {ultimo}')