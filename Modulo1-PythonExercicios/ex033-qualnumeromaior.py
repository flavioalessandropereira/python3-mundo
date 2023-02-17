a = float(input('Digite primeiro número: '))
b = float(input('Digite segundo número: '))
c = float(input('Digite o terceiro número: '))

#Verificando o menor número
menor = a
if b<a and b<c:
     menor = b
if c<a and c<b:
    menor = c
#verificando o maior número
maior = a
if b>a and b>c:
    maior =b
if c>a and c>b:
    maior = c
print('O menor número foi: {}'.format(menor))
print('O maior número foi: {}'.format(maior))