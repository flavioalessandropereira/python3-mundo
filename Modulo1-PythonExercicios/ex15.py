dias = int(input('Qtos dias de aluguel: '))
km=float(input('Qtos km percorridos: '))

pago = (dias *60.0) + (km * 0.15)


print('O total a pagar é R${:.2f}'.format(pago))