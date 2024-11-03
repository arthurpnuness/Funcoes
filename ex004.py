'''Faça um algoritmo que leia cinco notas e faça a média das notas, após isso informe a situação do aluno: 
>= 7 			Aprovado 
4 <= e < 7 	    Recuperação 
< 4 			Reprovado 
Utilize três funções para apresentar a situação do aluno.
'''


def notas():
    contador = 0
    nota = 0
    while contador < 5:
        nota += float(input('Digite as suas notas: '))
        contador += 1
    return nota

def calcula_media(nota):
    media = nota / 5
    if media >= 7:
        print(f'Voce foi aprovado com uma média de: {media}')
    elif media <= 4 and media < 7:
        print(f'Voce ficou em recuperação com uma média de: {media}')
    else:
        print(f'Voce foi reprovado com uma média de: {media}')
    return media

def main():
    nota = notas()
    media = calcula_media(nota)

main()

