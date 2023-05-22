primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1
print('Fim')