'''
comentários

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''

#exercicio:

nome=str(input('Digite seu nome: '))
km=float(input('Digite os km percorridos: '))
dias=int(input('Digite quantos dias ficou alugado: '))

kmAtual=float(7580.64)

totAluguel=float((60*dias)+(0.15*km))
totKm=float(kmAtual+km)

print('\n\nNome do locador: {}.\nKM percorridos durante locação: {}.\nValor do aluguel: {}.\nKilometragem atual do carro: {}.'.format(nome,km,totAluguel,totKm))