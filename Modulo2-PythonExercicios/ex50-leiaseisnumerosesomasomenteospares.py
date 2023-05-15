soma = 0
pares = 0
for c in range (1, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma = soma + numero
        pares = pares + 1
print(f'Vc informou {pares} pares e o total da soma é: {soma}')