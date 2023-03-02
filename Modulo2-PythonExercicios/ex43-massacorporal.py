peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura ** 2) #altura ao quadrado

print('O IMC é {:.2f} '.format(imc), end = '')

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
