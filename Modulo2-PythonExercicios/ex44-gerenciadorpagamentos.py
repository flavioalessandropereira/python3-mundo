print ('{:=^40}'.format(' LOJA FAP '))

preco = float(input('Preço das compras: R$ '))

print ( ''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opcao = int (input('Qual opção de pagamento: '))

if opcao == 1:
    pagar = preco * 0.9
    print('Pagamento à vista dinheiro/cheque, desconto de 10%, o valor pagar é R$ {:.2f}.'.format(pagar))
elif opcao == 2:
    pagar = preco * 0.95
    print('Pagamento à vista com cartão, desconto 5%. Valor pagar R$ {:.2f}.'.format(pagar))
elif opcao == 3:
    pagar = preco /2
    print('Pagamento no cartão em 2x de parcelas R$ {:.2f}.'.format(pagar))
elif opcao == 4:
    pagar = (preco * 1.2)
    parcelas = int(input('Quantas parcelas? '))
    pagar1 = pagar / parcelas
    print('Pagamento em {} x de R$ {:.2f}.'.format(parcelas,pagar1))
else:
    print('Falha, opção de pagamento não RECONHECIDO!')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, pagar) )