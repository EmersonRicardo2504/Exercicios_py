#Faça um Programa que peça dois números e imprima o maior deles.

body = "\n Nós informe dois numero e iremos retornar o valor mais alto =)\n"
print(body) 

num_1 = int(input("Coloque o primeiro valor: "))
num_2 = int(input("Coloque o segundo valor: "))

if num_1 > num_2:
    print(f"{num_1} é maior que o {num_2}")

elif num_2 > num_1:
    print(f"{num_2} é maior que o {num_1}")
