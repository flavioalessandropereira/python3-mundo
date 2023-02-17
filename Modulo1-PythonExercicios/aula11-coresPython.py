print('\033[4;30;45mOlá, Mundo!\033[m')

print('\033[7;33;44mFlavio A Pereira!\033[m')

a = 3
b = 5
print('Os valores são \033[31m{} \033[me \033[34m{} \033[m!!!'.format(a,b))

nome = 'Guanabara'

cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {} {} {}!!'.format('\033[32m',nome,'\033[m'))

print('Olá! Blz, {}{}{}!!'.format(cores['amarelo'],nome,cores['limpa']))

print('\033[31m                JOGO DE ADIVINHAÇÃO')