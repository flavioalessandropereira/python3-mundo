soma = contador = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma = soma + numero

print(f'Foram digitados {contador} e soma dos números digitados = {soma}')