class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    idade = 15

    def saudacao(self):
        print('Olá Pessoas!')

# Cria um novo objeto da classe Pessoa
matheus = Pessoa()

# Output: 15
print(matheus.idade)

# Output: <bound method Pessoa.saudacao of <__main__.Pessoa object at 0x...>>
print(matheus.saudacao)

# Chamando o metodo saudacao()
# Output: "Olá Pessoas!"
matheus.saudacao()
