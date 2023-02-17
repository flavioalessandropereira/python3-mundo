velocidade=float(input('Digite a velocidade que passou no radar: '))

if velocidade > 80.00:
    print('Vc foi multado! O valor a pagar é: R$ {:.2f}'.format((velocidade -80.00) *7))

print('Tenha um bom dia! Dirija com segurança!')