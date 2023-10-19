solicitação =  '''

        Faça um Programa que leia 4 notas, mostre as notas e a média na tela .

'''
print(solicitação)

def aluno_1():

    # solicitando nome 
    nome = input("Coloque seu nome: ")
    
    #solicitando notas 
    nota_1 = int(input(f"Coloque a primeira nota {nome}: "))
    while nota_1 >=11:
        nota_1 = int(input(f"Coloque a primeira nota {nome}: "))

    nota_2 = int(input(f"Coloque a segunda nota {nome}: "))
    while nota_2 >=11:
        nota_2 = int(input(f"Coloque a segunda nota {nome}: "))

    nota_3 = int(input(f"Coloque a terceira nota {nome}: "))
    while nota_3 >=11:
        nota_3 = int(input(f"Coloque a terceira nota {nome}: "))
    
    nota_4 = int(input(f"Coloque a quarta nota {nome}: "))
    while nota_4 >=11:
        nota_4 = int(input(f"Coloque a quarta nota {nome}: "))

    #nota de corte
    nota_corte = 4

    #soma dos valores 
    soma = (nota_1  + nota_2 + nota_3 + nota_4) // nota_corte

    #estrutura de decição, aprovado // reprovado - saida de valores 
    if soma <= 4:
        print(f'\n\t{nome}, você foi reprovado com a media {soma}! \n\n\t Tente novamente!')
    
    elif soma >= 5:
        print(f"\n\t{nome}, sua media final foi de {soma}, você foi aprovado!  \n\n\t Parabéns")

    

aluno_1()




