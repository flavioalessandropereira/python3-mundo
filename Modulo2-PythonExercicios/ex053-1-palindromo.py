frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
juntar = ''.join(palavras)

inverso = ''
print(frase)
print(palavras)
print(len(juntar))

for letra in range(len(juntar)-1, -1, -1):
    inverso = inverso + juntar[letra]
print(f'Frase digitada: {juntar}')
print(f'Frase invertida: {inverso}')

if juntar == inverso:
    print('A frase é PALÍNDROMO')
else:
    print('A frase náo é Palindromo')
