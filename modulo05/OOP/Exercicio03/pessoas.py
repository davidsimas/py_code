class Pessoas:

    nome = ""
    sobrenome = ""
    idade = 0
    data_nascimento = ""

    def __str__(self):
        return f"{self.nome} - {self.sobrenome} - {self.idade} - {self.data_nascimento}"