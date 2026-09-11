def somar(a,b,c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Everton Henrique
    """
    s = a + b + c
    print(f'A soma vale {s}')

# Programa Principal
"""somar(3,2,5)
somar(2,3,4)
somar(8,4)"""
help(somar)