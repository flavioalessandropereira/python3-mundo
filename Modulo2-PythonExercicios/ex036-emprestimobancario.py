valor_casa = float(input('Qual o valor do imóvel:R$ '))
salario = float(input('Qual o seu salário bruto: R$'))
anos_pagar = int(input('Qtos anos pretende pagar: '))

meses_pagar = anos_pagar * 12
prestacao = valor_casa / meses_pagar

nao_pode_exceder = salario * 0.30

if nao_pode_exceder < prestacao:
    print('O valor dos 30% de seu salário é R$ {:.2f} , será destinado a  prestação do financiamento de R$ {:.2f}.'.format(nao_pode_exceder, prestacao))
    print('\033[1;31mEmpréstimo NEGADO\033[m')
else:
    print('\033[1;34mPARABÉNS!ACABOU DE FINANCIAR UMA CASA.\033[m A prestação \033[1;32m R$ {:.2f}.\033[m'.format(prestacao))