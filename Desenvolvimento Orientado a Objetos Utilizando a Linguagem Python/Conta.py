class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    @property
    def get_saldo(self):
        return self.saldo

    @get_saldo.setter
    def set_saldo(self, saldo):
        if saldo < 0:
            print('O saldo não pode ser negativo')
        else:
            self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        self.saldo += valor
        print("Deposito realizado com sucesso")

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo Atual: ", self.saldo)
