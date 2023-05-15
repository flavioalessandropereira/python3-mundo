peso_menor = 0
peso_maior = 0
for pessoas in range (1, 4):
    peso = int(input(f'Peso da pessoa {pessoas}: '))

    if pessoas == 1:
        peso_menor = peso
        peso_maior = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f'peso maior {peso_maior} kg.')
print(f'peso menor {peso_menor} kg.')