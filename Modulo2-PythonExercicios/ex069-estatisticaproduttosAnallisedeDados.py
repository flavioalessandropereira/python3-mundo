mulher20 = masculino= maior18=0
while True:
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]? ')).strip().upper()[0]
        if idade >=18:
            maior18 += 1
        if sexo == 'M':
            masculino += 1
        if sexo == 'F' and idade < 20:
            mulher20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continunar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoa com maior de 18 anos = {maior18}. Homens cadastrados {masculino}. Mulheres com menos 20 anos = {mulher20}')
print('fim')