sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
