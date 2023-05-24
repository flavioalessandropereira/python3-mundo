from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')

total = 0
contador = 0
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR?[P/I] ')).strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. Total {total}. ',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print(f'Vc ganhou')
            vitoria = vitoria + 1
        else:
            print('Vc perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Vc ganhou')
            vitoria = vitoria + 1
        else:
            print('Vc perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Vc venceu {vitoria} partidas.')
