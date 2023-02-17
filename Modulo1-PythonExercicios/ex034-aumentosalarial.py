salario = float(input('Digite o seu salário: '))

if salario <= 1250.00 :
    salario_atual= salario * 1.15
else:
    salario_atual = salario *1.10
print('O seu salário reajustado será R$ {:.2f}'.format(salario_atual))