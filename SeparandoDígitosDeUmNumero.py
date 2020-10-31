'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

num=int(input('Digite um número: '))

numS=str(num)

tam=len(numS)

print(tam)

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
dezenaMilhar = num // 10000 % 10
centenaMilhar = num // 100000 % 10
milhao = num // 1000000 % 10
dezenaMilhao = num // 10000000 % 10
centenaMilhao = num // 100000000 % 10
bilhao = num // 1000000000 % 10
dezenaBilhao = num // 10000000000 % 10
centanaBilhao = num // 100000000000 % 10
trilhao = num // 1000000000000 % 10

if tam == 0:
    print('0')
elif tam == 1:
    print('o num {} tem apenas a {}, apenas.'.format(num,unidade))
elif tam == 2:
    print('o num {} tem apenas a {} e {}, apenas.'.format(num,unidade,dezena))
elif tam == 3:
    print('o num {} tem apenas a {}, {} e {}, apenas.'.format(num,unidade,dezena,centena))
elif tam == 4:
    print('o num {} tem apenas a {}, {}, {} e {}, apenas.'.format(num,unidade,dezena,centena,milhar))
elif tam == 5:
    print('o num {} tem apenas a {}, {}, {}, {} e {}, apenas.'.format(num,unidade,dezena,centena,milhar,dezenaMilhar))
elif tam == 6:
    print('o num {} tem apenas a {}, {}, {}, {}, {} e {}, apenas.'.format(num,unidade,dezena,centena,milhar,dezenaMilhar,centenaMilhar))
else:
    print('\nInválido\n\n');
   

