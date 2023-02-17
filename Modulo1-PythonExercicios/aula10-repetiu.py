n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

m = (n1+n2)/2

print('Sua média foi {:.2f}'.format(m))

if m>= 6.0:
    print('Vc passou !')
else:
    print('Vc reprovou !')