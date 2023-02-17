#import math #importa toda a biblioteca math
from math import trunc
from math import sqrt

n = float(input('Digite um número decimal: '))

#print('O numero digitado é {} e sua parte inteira é {}'.format(n,math.trunc(n)))

print('O numero digitado é {} e sua parte inteira é {}'.format(n,trunc(n)))

num1 = float(input('Digite o segundo número decimal: '))
print('O valor digitado é {} e sua parte inteira é {}'.format(num1,int(num1)))

raiz = 25
print(sqrt(raiz))