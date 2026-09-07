from random import choice, randint, shuffle
aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
