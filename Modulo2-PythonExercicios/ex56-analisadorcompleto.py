somaidade = 0
mediaidade = 0
maior_idade_homem = 0
nome_velho = ''
totalmulher20 = 0

for pessoas in range(1,4):
    print(f'-----{pessoas} PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade

    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem =idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in "Ff" and idade < 20:
        totalmulher20 += 1

print(f'A média de idade do grupo é: {somaidade/2} anos.')
print(f'O nome do homem mais velho é {nome_velho} e tem {maior_idade_homem} anos.')
print(f'Mulheres com menos de 20 anos =  {totalmulher20} mulheres.')