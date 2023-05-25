valor = int(input('Digite o valor a sacar: R$ '))

total = valor

cedulaatual = 100
totalcedula = 0

while True:
    if total >= cedulaatual:
        total = total - cedulaatual
        totalcedula += 1
    else:
        if totalcedula > 0:
             print(f'Total {totalcedula} cédulas de RS {cedulaatual}')
        if cedulaatual == 100:
            cedulaatual = 50
        elif cedulaatual == 50:
            cedulaatual = 20
        elif cedulaatual == 20:
            cedulaatual = 10
        elif cedulaatual == 10:
            cedulaatual = 5
        elif cedulaatual == 5:
            cedulaatual = 1
        totalcedula = 0
        if total == 0:
            break