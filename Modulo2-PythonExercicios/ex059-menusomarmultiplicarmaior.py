n1 = int(input('Primeiro Valor: '))
n2 = int(input('sSegundo Valor: '))
opcao = 0

while opcao != 5:

    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')

    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma de {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'a multiplicacao {n1} * {n2} = {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print( f'O maior entre {n1} é {n2} é o {maior}')
    elif opcao == 4:
        print('Informe novos valores!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(n1)
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('opcao inválida. tente novamente: ')
    print('=-=' * 10)
print('Fim do programa.')