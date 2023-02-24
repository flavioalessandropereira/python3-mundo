from datetime import date

ano_atual = date.today().year

ano_nasc = int(input('Ano de Nascimento: '))

idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if idade  == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda fatam {} anos para o alistamento.'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será: {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos atrás.'.format(saldo))
    ano = ano_atual - saldo
    print('Vc deveria ter alistado em {}.'.format(ano))