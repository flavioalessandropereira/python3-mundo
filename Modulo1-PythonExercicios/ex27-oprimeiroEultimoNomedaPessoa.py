n = str(input('Digite o seu nome completo: ')).strip()

nome = n.split()

print('Muito prazer em te conhecer!')

print('O seu primerio nome é: {}'.format(nome[0]))

print('O seu nome de família é: {}'.format(nome[len(nome)-1]))

