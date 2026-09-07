nome = str(input('Qual é o seu nome? '))
if nome == 'Everton':
    print('Que nome Forte! ')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome Feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia , {nome}!')