

proposta = '''

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
                                    As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".

'''


# elaborando perguntas 




def perguntas(): 

    nome = input("\tColoque seu nome:\t\n")

    responda = """\tResponda com [Sim] para respostas positivas ou [Não] resposatas negativas!\t\n"""
    print(responda)

    # pergunta 1
    pergunta_1 = input(f"\t{nome}, Telefonou para vatima ?\n")
    while pergunta_1 != "Sim" and pergunta_1 != "Não":
        pergunta_1 = input(f"\t{nome}, Telefonou para vatima ?\n")

    # pergunta 2
    pergunta_2 = input(f"\t{nome}, Esteve no local do crime ?\n")
    while pergunta_2 != "Sim" and pergunta_1 != "Não":
        pergunta_2 = input(f"\t{nome}, Esteve no local do crime ?\n")

    # pergunta 3
    pergunta_3 = input(f"\t{nome}, Mora perto da vítima ?\n")
    while pergunta_3 != "Sim" and pergunta_3 != "Não":
        pergunta_3 = input(f"\t{nome}, Mora perto da vítima ?\n")

    # pergunta 4
    pergunta_4 = input(f"\t{nome}, Devia para a vítima ?\n")
    while pergunta_4 != "Sim" and pergunta_4 != "Não":
        pergunta_4 = input(f"\t{nome}, Devia para a vítima ?\n")

    # pergunta 5
    pergunta_5 = input(f"\t{nome}, Já trabalhou com a vítima ?\n")
    while pergunta_5 != "Sim" and pergunta_5 != "Não":
        pergunta_5 = input(f"\t{nome}, Já trabalhou com a vítima ?\n")
    
    # variaveis contadoras
    resp_posi = 0
    resp_neg = 0

    # decição pirmira pergunta
    if pergunta_1 == "Sim":
        resp_posi += 1
        
    if pergunta_1 == "Não":
        resp_neg += 1

    # decição segunda pergunta
    if pergunta_2 == "Sim":
        resp_posi +=1
    
    if pergunta_2 == "Não":
        resp_neg +=1

    # decição terceira pergunta
    if pergunta_3 == "Sim":
        resp_posi +=1
    
    if pergunta_3 == "Não":
        resp_neg +=1
    

# decição quarta pergunta
    if pergunta_4 == "Sim":
        resp_posi +=1
    
    if pergunta_4 == "Não":
        resp_neg +=1

    # decição quinta pergunta
    if pergunta_5 == "Sim":
        resp_posi +=1
    
    if pergunta_5 == "Não":
        resp_neg +=1

    # impressão caso ele seja culpado
    if resp_posi == 5:
        print(f"\n\t******\t{nome}, teve",resp_posi,"respostas positivas!\t******")
        print(f"\n\t******\t{nome}, assassino!\t******")

    # impressão caso ele seja suspeito
    if resp_posi == 2:
        print(f"\n\t******\t{nome}, teve",resp_posi,"respostas positivas!\t******")
        print(f"\n\t******\t{nome}, suspeito!\t******")

     # impressão caso ele seja cumplice 
    if resp_posi >=3 and resp_posi <=4:
        print(f"\n\t******\t{nome}, teve",resp_posi,"respostas positivas!\t******")
        print(f"\n\t******\t{nome}, cumplice!\t******")

    # impressão caso ele seja inocente
    if resp_neg == 5:
        print(f"\n\t******\t{nome}, teve",resp_neg,"respostas negativas!\t******\n" )
        print(f"\n\t******\t{nome}, inocente!\t******\n")

perguntas()
    
    
 

    