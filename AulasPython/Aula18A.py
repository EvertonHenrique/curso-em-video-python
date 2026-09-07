teste = list()
teste.append('Everton')
teste.append(30)
galera = list()
galera.append(teste[:])
teste[0] = 'Mauro'
teste[1] = 52
galera.append(teste[:])
print(galera)