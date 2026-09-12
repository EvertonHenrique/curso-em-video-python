def fatorial(n, show=False):
    """
    => Calcula o fatorial de um número
    :param n: O número que será calculado
    :param show: É a operação completa do fatorial e será mostrada ou não
    :return: Retorna o valor do fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            print(' x ' if c > 1 else ' = ', end=' ')
        f *= c
    return f


# Programa Principal
print(fatorial(10, show=True))
help(fatorial)