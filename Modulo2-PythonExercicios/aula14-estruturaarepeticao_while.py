'''for c in range(1, 10):
    print(c)
print('fim')'''

'''c= 1
while c < 10:
    print(c)
    c+=1
print('fim')'''

'''n = 1

while n != 0:
    n = int(input("Digite um valor: "))
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N]: ')).upper()
print('FIM')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par = par +1
        else:
            impar = impar + 1
print(f'Qtde numeros pares digitados  = {par} ')
print(f'Qtde numeros impares digitados  = {impar} ')
