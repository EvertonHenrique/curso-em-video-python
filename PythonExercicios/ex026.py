frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A 1ª letra A aparece na {frase.find("A")+1} posição')
print(f'A última letra A aparece na {frase.rfind("A")+1} posição.')