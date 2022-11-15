# Classe Mãe
class Conta:

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print("Passando pelo Construtor Conta")

    def __str__(self):
        return f"Número de Conta:> {self.numero}\nTipo de Conta:> {self.tipo}"