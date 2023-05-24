from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')


soma = 0
contador = 0
while True:
    computador = randint(0, 10)
    print(computador)

    print('=-' * 20)
    jogador = int(input('Diga um valor: '))
    parimpar = str(input('Par ou Ímpar?[P/I]')).strip()[0].upper()

    soma = jogador + computador
    resultado = soma % 2

    if parimpar == 'P':
        if resultado == 0:
            print('-' *20)
            print(f'Voce jogou {jogador} e o computadador {computador}. Total de {soma} DEU PAR')
            print('-' * 20)
            print('Você VENCEU')
            print('Vamos jogar novamente ...')

    if parimpar == 'I':
        if resultado != 0:
            print('-' *20)
            print(f'Voce jogou {jogador} e o computadador {computador}. Total de {soma} DEU IMPAR')
            print('-' * 20)
            print('Você VENCEU')
            print('Vamos jogar novamente ...')
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        print('GAME OVER!')
        break