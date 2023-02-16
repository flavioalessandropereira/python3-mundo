nome= input('Qual seu nome? ')

print('Prazer em te conhecer {}!'.format(nome))

print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))

print('Prazer em te conhecer {:=^20}!'.format(nome))

n1=int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2

print('A soma é {},  o produto é {} e a divisao {:.3f}'.format(s,m,d), end= ' ')
print('Divisão inteira é {} e potência é {}'.format(di,exp))