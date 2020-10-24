'''
MODULOS DE COD
'''

#declara modulo
#import math

#para gerar números aleatorios
import random

#algumas bibliotecas precisam ser baixadas no computador
#consultar https://pypi.org/
import emoji

#declara modulo especifico
from math import sqrt

n1=int(input('Digite um número: '))

raiz=math.sqrt(num)

print('raiz quadrada de {} é {}.'.format(n1,raiz))

'''
*******************************************************************************
'''

n2=random.randint()

print('aleatorio: {}'.format(n2))

'''
*******************************************************************************
'''

#forma de printar o emoji pode variar de modolo para modolo
print(emoji.emojize('Printando emoji: :earth_americas', use_aliases=True))