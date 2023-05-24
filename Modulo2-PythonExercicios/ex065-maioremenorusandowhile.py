resposta = 'S'
contador = 0
soma = media = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    contador = contador + 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resposta = str(input('Deseja continuar [S/N]? ')).strip()[0].upper()

   #if resposta == 'N':
    #    media = soma / contador

media = soma / contador
print('Programa finalizado')
print(f'vc digitou {contador} números. O total da soma é {soma } e a média é {media}.')
print(f'O maior número digitado foi {maior} e o menor número foi {menor}')
