'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
'''


palavra=str(input('Digite algo: '))

print(palavra.upper())
print(palavra.lower())


spaces=palavra.count(' ')
tam=len(palavra)

a=tam-spaces

palavra=palavra[:a]


print('\nTamanho: {}'.format(a))



