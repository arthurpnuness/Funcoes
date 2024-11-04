'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
Entenda o Cálculo Necessário: Para aplicar o imposto, você precisa:

Transformar a porcentagem de taxaImposto em um valor decimal (dividindo por 100).
Multiplicar esse valor pelo custo para encontrar o valor do imposto.
Somar esse imposto ao custo para obter o valor final.
Formule um Passo a Passo:

Receber a taxaImposto e o custo.
Calcular o imposto e somá-lo ao custo.
Retornar o valor final com o imposto incluso.'''


def soma_imposto(taxa_imposto, custo): # Função para calcular o valor do imposto como uma porcentagem do custo
    imposto = custo * (taxa_imposto / 100)
    custo_final = custo + imposto
    return custo_final

def altera(taxa_imposto, custo): # Função para calcular a quantidade de camisetas e o valor a ser pago pelo cliente 
    qtd = int(input('Digite quantas camisetas voce quer adquirir: '))
    if qtd > 4:
        valor_final = 50 * qtd
        print(f'Voce adquiriu {qtd} camisetas no valor de R${valor_final:.2f} e nao vai pagar imposto')
    else:
        custo_final = soma_imposto(taxa_imposto, custo)
        total = qtd * custo_final
        print(f'Você adquiriu {qtd} camisetas e vai pagar o valor de R${total:.2f} com imposto.')

def main(taxa_imposto, custo):  # Essa função chama a função altera para realizar a operação de compra e calcular o imposto, se aplicável
    altera(taxa_imposto, custo)

# Define o valor do imposto e o custo inicial do item
taxa_imposto = 10  
custo = 50.00  

# Inicia o programa chamando a função main com os argumentos necessários
main(taxa_imposto, custo)

