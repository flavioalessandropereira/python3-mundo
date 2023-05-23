print('='* 30)
print('{:^30}'.format('Fibonnacci'))
print('='* 30)

n = int(input('Digite o número: '))

termo1 = 0
termo2 = 1
contador = 3
print(f'{termo1} -> {termo2} -> ', end='')
while contador <= n:
    termo3 = termo2 + termo1
    print(f'{termo3} -> ', end='')
    termo1 = termo2
    termo2 = termo3

    contador = contador + 1




print(' Fim', end='')
