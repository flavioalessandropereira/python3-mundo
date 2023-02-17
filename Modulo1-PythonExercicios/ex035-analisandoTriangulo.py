def linhas ():
    print('-=' *20)
linhas()
print('Analisador de triângulo')
linhas()

r1 = float(input('1ª segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3ºsegmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode formar um triângulo')
else:
    print('Não pode formar um triângulo')