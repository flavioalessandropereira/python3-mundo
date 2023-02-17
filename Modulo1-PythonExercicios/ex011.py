altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura da parede em metros: '))

area = altura * largura
tintas = area /2

print('A largura da parede {}m X altura da parede {}m = {} m2.'.format(altura,largura,area))
print('Utilizará {} litros de tinta.'.format(tintas))