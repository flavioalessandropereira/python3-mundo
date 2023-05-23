primeiro = int(input('Primeiro Termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
contador = 1
inicial = 10
total = 0
mais =10
while mais != 0 :
    total = total + mais
    while contador <= total:
        print(f'{termo} ', end='')
        termo = termo + razao
        contador = contador + 1
    print('pausa')
    mais = int(input('qtos termos a mais que vc quer? '))
print(f'Progressao Aritmética com {total} termos mostrados.')
print('fim')

