def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: não mostra o retorno
    Função criada por Everton Henrique
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')

# Programa Principal
contador(2, 1, 7)
help(contador)