nome=str(input('Digite seu nome completo: ')).strip()

maiuscula = nome.upper()
minuscula = nome.lower()

print('Anlisando seu nome...')


print('Seu nome é letras maiúsculas: ', format(maiuscula))
print('Seu nome em letras minúsculas> ', format(minuscula))
print('Seu nome tem ao todo {} letras.'.format((len(nome)-nome.count(' '))))

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split() #converte o nome inteiro em listas
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))