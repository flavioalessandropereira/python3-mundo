total = preco1000 = menorpreco = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total = preco + total
    contador += 1

    if preco > 1000:
        preco1000 += 1

    if contador == 1:
        menorpreco = preco
        barato = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print('------ FIM DO PROGRAMA --------')
print(f'O produto mais barato é {barato}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {preco1000} produtos que custaram mais de R$1000.')

