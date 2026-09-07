print('-=' * 30)
print('1 - Binario \n2 - Hexadecimal \n3 - Octal')
num = int(input('Escolha o numero: '))
opção = int(input('Opção: '))
if opção == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} covertido para HEXADECIMAL é igual a {hex(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido a OCTAL  é igual a {oct(num)[2:]}')
else:
    print('OPÇÃO INVALIDA! tente novamente!')