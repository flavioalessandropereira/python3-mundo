distancia = float(input('Qual a distância da viagem em km: '))

if distancia <= 200 :
    print('O valor da viagem é {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da viagem é {:.2f}'.format((distancia * 0.45)))