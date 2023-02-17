import math

num = int (input('Digite um numero: '))
raiz =math.sqrt(num)

print('A raíz de {} é igual a {}'.format(num, raiz))

print('A raíz de {} é igual a {}'.format(num, math.ceil(raiz)),'arredondei para cima')

print('A raíz de {} é igual a {}'.format(num, math.floor(raiz)),'arredondei para baixo')

print('A raíz de {} é igual a {:.2f}'.format(num,raiz),'com duas casa decimais')