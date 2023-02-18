nome = str(input('qual seu nome: '))

if nome == 'Flavio':
    print('Q NOME BONITO! ')
elif nome == "Pedro" or nome =='Maria':
    print('seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('belo nome feminino.')
else:
    print('q nome normal')
print('Tenha um bom dia {}.'.format(nome))