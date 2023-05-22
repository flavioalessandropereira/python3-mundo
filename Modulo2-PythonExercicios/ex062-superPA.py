primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        contador = contador + 1

    print('pausa')
    mais = int(input('qtos temos vc quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')