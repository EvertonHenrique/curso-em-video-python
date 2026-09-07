extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez'
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numeros = int(input('Digite um número (Exibirá o numero por Extenso) de 0 e 20: '))
    if 0 <= numeros <= 20:
        break
print(f'O número digitado por extenso é {extenso[numeros]}.')