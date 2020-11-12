'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

cidade=str(input('Digite o nome de uma cidade: '))

cidade2=cidade.upper()

ini=cidade2.find('SANTO')

print(ini)

if ini==0:
    print('\nO primeiro nome da cidade é Santo')
elif ini==-1:
    print('\nPalavra não existe')
else:
    print('\nO primeiro nome da cidade NÃO é Santo')
