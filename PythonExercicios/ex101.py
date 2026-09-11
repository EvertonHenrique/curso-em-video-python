def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


nascimento = int(input('Em que ano você nasceu? '))
print(f'{voto(nascimento)}')