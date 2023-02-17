import math

cateto_oposto = float(input('Digite o comprimento do cateto adjacente:'))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print('Cateto oposto: {} / Cateto adjacente: {} e a hipotenusa é {}.'.format(cateto_oposto,cateto_adjacente,hipotenusa))