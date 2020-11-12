'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase=str(input('Digit uma frase: '))
fraseUP=frase.upper()

print('A letra A aparece {} vezes na frase.\nA primeira aparece na posição {}.\nA última aparece na posição {}.'.format(fraseUP.count('A'),fraseUP.find('A'),fraseUP.rfind('A')))
'''
PrimeiraEUltimaString.py
'''