from random import shuffle
n1 = str(input('ALUNO 1: '))
n2 = str(input('ALUNO 2: '))
n3 = str(input('ALUNO 3: '))
n4 = str(input('ALUNO 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ORDEM ESCOLHIDA FOI: ')
print(lista)

