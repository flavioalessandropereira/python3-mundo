numero = int(input('Digite um numero: '))
total = 0
for contador in range ( 1, numero+1):
    if numero % contador == 0:
        print('\033[33m', end ='')
        total += 1
    else:
        print('\033[m', end = '')
    print(contador, end =' ')

print(f'\n\033[mO numero {numero} foi divisível por {total} vezes.')

if total == 2:
    print( f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')