frase = str(input('Digite uma frase: ')).strip().upper() #tirei todos os espaços

palavras = frase.split() #fiz uma lista
junto = ''.join(palavras) #juntei tudo

inverso = ''

for letra in range(len(junto) -1, -1,-1):
    inverso = inverso +junto[letra]
print(junto, inverso)

if junto == inverso:
    print(f'A frase: {frase}, é Polindromo!')
else:
    print('A frase não é um Palíndromo.')