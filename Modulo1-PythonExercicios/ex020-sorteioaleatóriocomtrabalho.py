import random

n1 = str(input('aluno1: '))
n2 = str(input('aluno2: '))
n3 = str(input('aluno3: '))
n4 = str(input('aluno4: '))

lista =[n1,n2,n3,n4]
random.shuffle(lista)


print('A ordem de apresentação: ')
print(lista)