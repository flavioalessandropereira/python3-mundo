'''import random
computador = random.randint(0,10)'''

from random import randint
computador = randint (0,10)
print('Sou seu computador, e pensei num número entre 0 e 10.')
print('Será que vc consegue adinhar?')
print(computador)
acertou = False
palpites = 0
while not acertou:
    jogador= int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
        break
    else:
        if jogador < computador:
            print('mais... Tente mais uma vez')
        else:
            print('menos...Tente mais uma vez')

print(f'Vc precisou de {palpites}, para acertar o numero.')