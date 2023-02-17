numero = int(input('Digite um número inteiro: '))

parimpar = numero % 2

if parimpar == 0 :
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é impar.' .format(numero))