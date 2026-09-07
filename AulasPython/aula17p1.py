num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
'num.pop(3)'
num.insert(2, 0)
if 5 in num:
    num.remove(5)
else:
    print('Não tem o numero 5 na lista')
print(num)
print(f'A lista tem {len(num)} elementos.')