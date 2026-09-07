frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {inverso} é a palavra {junto}')
if inverso == junto:
    print('A frase é um PALINDROMO!')
else:
    print('A frase não é um PALINDROMO!')