'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random


aluno1=str(input('Digite o nome do aluno: '));
aluno2=str(input('Digite o nome do aluno: '));
aluno3=str(input('Digite o nome do aluno: '));
aluno4=str(input('Digite o nome do aluno: '));

n=random.randrange(4);

vet=[]
for i in vet[i]:
    vet[i]++;

if vet[1]==vet[2] or vet[1]==vet[3] or vet[1]==vet[4] or vet[i]>4:
    vet[1]=random.randrange(4);
elif vet[2]==vet[2] or vet[1]==vet[3] or vet[1]==vet[4] or vet[i]>4:
    vet[2]=random.randrange(4);
elif vet[3] == vet[2] or vet[1] == vet[3] or vet[1] == vet[4] or vet[i] > 4:
    vet[3]=random.randrange(4);
elif vet[4] == vet[2] or vet[1] == vet[3] or vet[1] == vet[4] or vet[i] > 4:
    vet[4]=random.randrange(4);

print('\n\nPrimeiro aluno cadastrado {}.\nSegundo aluno cadastrado {}.\nTerceiro aluno cadastrado {}.\nQuarto aluno cadastrado {}.\n\n'.format(aluno1,aluno2,aluno3,aluno4));

for i in 4:
    if n == 1:
        print('\nO aluno {} - {}, limpará o quadro.'.format(n, aluno1));
    elif n == 2:
        print('\nO aluno {} - {}, limpará o quadro.'.format(n, aluno2));
    elif n == 3:
        print('\nO aluno {} - {}, limpará o quadro.'.format(n, aluno3));
    elif n == 4:
        print('\nO aluno {} - {}, limpará o quadro.'.format(n, aluno4));
