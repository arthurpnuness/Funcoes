'''O mercado QUIOSQUE está com uma promoção, comprando até 12 laranjas, o preço unitário é R$0,40, caso compre mais que 12 o valor cai para R$0,25. Faça um programa que leia o total de laranjas compradas e mostre o valor ao final da execução. Faça uma função que receba o total de laranjas e retorne o valor total da compra.
'''

valor_unitario = 0.40

def total_laranjas():
    laranjas = int(input('Quantas laranjas voce deseja comprar? '))

    if laranjas <= 12:
        valor_laranja = valor_unitario
        valor_compra = laranjas * valor_laranja
        print(f'O valor a ser pago é: R${valor_compra}')
    else: 
        valor_laranja = 0.25
        valor_compra = laranjas * valor_laranja
        print(f'O valor a ser pago é: R${valor_compra}')

total_laranjas()