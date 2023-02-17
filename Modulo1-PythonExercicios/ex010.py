real=float(input('Qto reais vc tem na carteira: '))
dolar= float(input('Qual a cotação do dólar hoje: '))

comprar = real / dolar

print('Vc tem R${} na carteira e pode comprar US${:.2f}.'.format(real,comprar))