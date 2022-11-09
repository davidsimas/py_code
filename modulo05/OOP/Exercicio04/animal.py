class Animal:
    raca = ""
    cor = ""
    idade = ""

    def __str__(self):
        return f"{self.raca} - {self.cor} - {self.idade}"