from math import sin, cos, tan, radians
angulo = float(input('Digite um número: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo}\nTem o SENO de {seno:.2f}\nTem o COSSENO de {cosseno:.2f}\nTem a TANGENTE de {tangente:.2f}')
