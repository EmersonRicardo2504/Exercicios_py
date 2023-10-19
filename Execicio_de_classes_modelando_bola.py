proposta = '''

        Classe Bola: Crie uma classe que modele uma bola:

            Atributos: Cor, circunferência, material
            Métodos: troca Cor e mostrar Cor


'''

print(proposta)

# criando a classe 
class bola():

    # adicionando função pra reconhecer caracteristicas do produto
    def __init__(self, cor, circunferencia, material):
        self.cor = cor 
        self.circunferencia = circunferencia
        self.material = material

# saida de valores conta com atribuiução e chamada
bola_1 = bola("Vermelha", "redonda", "pano")
print(bola_1.cor, bola_1.circunferencia, bola_1.material)



