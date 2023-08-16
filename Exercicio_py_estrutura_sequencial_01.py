#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input("informe um numero: ")
print(f"O numero informado foi: {numero}")

###########################################
### Segunda possivel resolução #############

def numero():

    valor_1 = (int(input("Coloque um valor inteiro: ")))

    if valor_1 % 2 == 0:
        print(f"O valor {valor_1} é dividido por 2.")

    if valor_1 % 2 == 1:
        print(f"O valor {valor_1} não dividido por 2.")

numero()