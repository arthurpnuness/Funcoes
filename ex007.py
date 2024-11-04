'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
O sistema deve receber um valor de hora entre 0 e 23 e de minutos entre 0 e 59.
'''

def saida(): # Função onde extraimos os dados
    hora = int(input('Digite a hora do dia (entre 0 e 23): '))
    minutos = int(input('Agora digite os minutos (entre 0 e 59): '))
    return hora, minutos

def conversao(hora, minutos): # Função de conversao
    if hora == 0:
        # Meia-noite (0 horas)
        print(f'A hora do dia é 12:{minutos} A.M')
    elif 1 <= hora <= 11:
        # Período da manhã
        print(f'A hora do dia é {hora}:{minutos} A.M')
    elif hora == 12:
        # Meio-dia
        print(f'A hora do dia é 12:{minutos} P.M')
    elif 13 <= hora <= 23:
        # Período da tarde/noite (convertendo para formato de 12 horas)
        conversao_hora = hora - 12
        print(f'A hora do dia é {conversao_hora}:{minutos} P.M')
    else:
        print('Deve ter algum erro na sua digitação')

def main(): # Chama as funções necessárias para que o programa funcione 
    hora, minutos = saida()
    conversao(hora, minutos)

# Executa o programa
main()