from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(), "6565", 0)

print(c1)
print("Nome: ", c1.get_nome(), " e ", "Telefone: ", c1.get_telefone())
print("Titular da Conta: ", conta.titular, "Número: ", conta.numero, "Seu saldo: ", conta.saldo)
conta.depositar(100)
print("Titular da Conta: ", conta.titular, "Número: ", conta.numero, "Seu saldo: ", conta.saldo)
conta.saque(50)
print("Titular da Conta: ", conta.titular, "Número: ", conta.numero, "Seu saldo: ", conta.saldo)
conta.extrato()
