from datetime import date

ano_atual = date.today().year
menor_idade = 0
maior_idade = 0
for pessoas in range(1,8):
    ano_nasc =  int(input(f'Pessoa {pessoas}. Digite ano de nascimento: '))
    idade = ano_atual - ano_nasc

    if idade < 21:
        menor_idade = menor_idade + 1
    else:
        maior_idade = maior_idade + 1

print(f'Pessoas menores de 21 anos, {menor_idade} pessoas.')
print(f'Pessoas maiores de 21 anos, {maior_idade} pessoas.')