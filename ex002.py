'''Faça um algoritmo que receba um valor e apresente o dobro e o triplo do valor.
Utilize duas funções para realizar os cálculos
'''

def dobro():
    valor = int(input('Digite um valor para calcularmos o dobro dele: '))
    dobro = valor * 2
    print(f'O Dobro de {valor} é: {dobro}')
    return dobro

def triplo():
    valor = int(input('Digite um valor para calcularmos o triplo dele: '))
    triplo = valor * 3
    print(f'O triplo de {valor} é: {triplo}')
    return triplo

valor1 = dobro()
valor2 = triplo()
