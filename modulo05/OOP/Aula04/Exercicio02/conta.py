class Conta:

    def __init__(self, numero, agencia, tipo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        print("Passando pelo Construtor Conta")

    def __str__(self):
        return f"Número de Conta: {self.numero}\nNome da Agência {self.agencia}\nTipo de Conta: {self.tipo}\n"