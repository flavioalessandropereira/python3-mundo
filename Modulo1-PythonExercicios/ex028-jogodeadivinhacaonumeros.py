import random
import time
#from random import randint
computador = random.randint(0,5) #faz o computador pensar

print("<>"*20)
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
print('<>'*20)


jogador = int(input('Em que número eum pensei: ')) #jogador tenta adivinhar
print('PROCESSANDO...')

tempo=time.sleep(2)

if jogador == computador:
    print('Parabéns!! Vc conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador,jogador))