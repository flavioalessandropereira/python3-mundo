def traco():
    print ('=' * 40)

traco()
print('{:^40}'.format('Calculo de uma Progressao Aritmética'))
traco()

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for contador in range(primeiro, decimo + razao ,razao):
    print(contador, end = ' -> ')
print('fim')

