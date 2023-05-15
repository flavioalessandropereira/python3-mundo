for c in range(1,6):
    print ('oi')
print ('fim')

for c in range(1,6):
    print (c)
print ('fim')


for c in range(6,0,-1):
    print (c)
print ('fim')

for c in range(0,7,2):
    print (c)
print ('fim')

n = int(input('Digite um numero: '))

for c in range (0,n+1):
    print(c)
print('fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range (i, f+1, p,):
    print(c)
print('fim')

#somatoria

s = 0
for c in range (0,4):
    n = int(input('Digite um numero: '))
    s = s+n
print('A somatoria é: {}'.format(s))