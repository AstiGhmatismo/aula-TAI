class Treinador:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print(self.nome, self.idade)
        print("")
class Pokemon:
    def __init__(self, nome, tipo, tipo2, apelido):
        self.nome = nome
        self.tipo = tipo
        self.tipo2 = tipo2
        self.apelido = apelido
    def exibirpoke(self):
        print(self.nome, self.tipo, self.tipo2, self.apelido)
        print(" ")
