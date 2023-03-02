from datetime import date

ano_atual = date.today().year

ano_nasc = int(input('Data Nascimento: '))

idade = ano_atual - ano_nasc

print('Você nasceu em {}, e sua idade é {}.'.format(ano_nasc, idade))

if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14:
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Júnior.')
elif idade <= 25:
    print('Categoria Sênior.')
elif idade > 25:
    print('Categoria Master')
