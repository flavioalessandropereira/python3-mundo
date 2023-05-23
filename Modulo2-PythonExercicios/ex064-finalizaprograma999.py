n = 0
contador = 0
soma = 0
n = int(input('para sair do programa digite [999]: '))
while n != 999:
    soma = (soma + n)
    contador += 1
    n = int(input('para sair do programa digite [999]: '))
print(f'Digitou {contador} vezes, para sair do programa e a somatória dos números é {soma}')
print('Fim')