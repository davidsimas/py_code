# Classe Mãe
class Conta:
    
    # Atributos com modificadores de acesso privado
    __agencia = "Blumenau"
    __numero_agencia = 101

    # Metodos Getters e Setters
    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    

    @property
    def numero_agencia(self):
        return self.__numero_agencia
    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        self.__numero_agencia = numero_agencia

    # Metodo ToString
    def __str__(self):
        return f"{self.agencia}; {self.numero_agencia}"
