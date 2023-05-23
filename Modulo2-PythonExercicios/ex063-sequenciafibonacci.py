print('-'*30)
print('{:^30}'.format('Fibonacci'))
print('-'*30)

n = int(input('qtos termos que vc quer mostrar? '))

t1 = 0
t2 = 1

print(('~'*30))
print(f'{t1} -> {t2}', end ='')

contador = 3
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' -> fim')
print(('~'*30))