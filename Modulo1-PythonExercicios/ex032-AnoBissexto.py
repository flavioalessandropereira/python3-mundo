import datetime
ano = int(input('Que ano vc quer analisar? Coloque 0 para analisar o ano atual:  '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0:
    print('O ano de {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))