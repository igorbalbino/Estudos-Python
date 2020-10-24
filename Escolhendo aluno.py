'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random


aluno1=str(input('Digite o nome do aluno: '))
aluno2=str(input('Digite o nome do aluno: '))
aluno3=str(input('Digite o nome do aluno: '))
aluno4=str(input('Digite o nome do aluno: '))

n=random.randrange(4)

print('Primeiro aluno cadastrado {}.\nSegundo aluno cadastrado {}.\nTerceiro aluno cadastrado {}.\nQuarto aluno cadastrado {}.'.format(aluno1,aluno2,aluno3,aluno4))


if n == 1:
    print('O aluno {} - {}, limpará o quadro.'.format(n,aluno1))
elif n == 2:
    print('O aluno {} - {}, limpará o quadro.'.format(n,aluno2))
elif n == 3:
    print('O aluno {} - {}, limpará o quadro.'.format(n,aluno3))
elif n == 4:
    print('O aluno {} - {}, limpará o quadro.'.format(n,aluno4))