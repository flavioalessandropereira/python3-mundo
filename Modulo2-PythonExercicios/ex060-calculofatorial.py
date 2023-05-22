'''from math import factorial

n = int (input( 'Digite um número para calcular fatorial: '))
f = factorial(n)

print(f'O fatorial {n} = {f}')'''


n = int (input( 'Digite um número para calcular fatorial: '))
contador = n
fator = 1
print(f'Calculando {n}! = ', end='')
while contador > 0:
    print(f'{contador} ', end = '')
    print(' x ' if contador > 1 else ' = ', end='')
    fator = fator * contador
    contador -= 1
print(f'{fator}')
