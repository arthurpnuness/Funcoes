'''Faça um algoritmo que apresente o seguinte menu:
1 - Sacar dinheiro
2 - Depositar dinheiro
3 - Mostrar saldo
4 - Sair
O saldo inicial da conta é 0. O sistema deve ter 5 funções: Mostrar o menu; sacar; depositar; saldo e main
'''

saldo = 0  # Definindo o saldo inicial como uma variável global

def menu():     # Função para exibir o menu e solicitar ao usuário uma opção
    print('1 - Sacar Dinheiro')
    print('2 - Depositar Dinheiro')
    print('3 - Mostrar Saldo')
    print('4 - Sair')
    opc = int(input('Digite a opção desejada (1 - 2 - 3 - 4): '))
    return opc

def saldo_da_conta():     # Função para exibir o saldo atual da conta
    global saldo
    print(f'Seu saldo atual é de R${saldo}')

def sacar_dinheiro():     # Função para realizar um saque da conta
    global saldo
    if saldo > 0:
        saque = int(input('Qual valor você gostaria de sacar: '))
        if saque <= saldo:
            saldo -= saque
            print(f'Saque de R${saque} realizado com sucesso.')
        else:
            print('Saldo insuficiente para esse saque.')
    else:
        print('Você não tem saldo suficiente.')
    
def depositar():     # Função para realizar um depósito na conta
    global saldo
    deposito = int(input('Quanto você deseja depositar na sua conta? '))
    saldo += deposito
    print(f'Agora você tem um saldo de R${saldo}')

def main():     # Função principal que controla o fluxo do programa
    while True:
        opcao = menu()
        if opcao == 1:
            sacar_dinheiro()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            saldo_da_conta()
        elif opcao == 4:
            print('Saindo do sistema.')
            break
        else:
            print('Opção inválida. Tente novamente.')

main() # Inicia o programa chamando a função principal

