s = 0
cont = 0
for c in range(3,501,2):
    if c % 3 == 0:
        print(c, end= ' ')
        s += c
        cont +=1
print()
print(f'A somatória de 0 a 500 sendo multiplos de 3 é: {s}, e contou {cont} vezes.')