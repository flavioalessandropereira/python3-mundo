contador = 1
while True:
    tabuada = int(input('Quer ver a tabuda de qual valor? '))
    if tabuada <= 0:
        break
    print('-' * 40)
    for contador in range(1, 11):
        fator = tabuada * contador
        print(f'{tabuada} x {contador} = {fator}')
    print('-' * 40)

print(f'O programa não executa tabuada menor ou igual a zero e vc digitou {tabuada}')