class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

    #Metodo get
    def get_nome(self):
        return self._nome

    #Metodo set
    def set_nome(self, nome):
        self._nome = nome

    #Metodo get para telefone
    def get_telefone(self):
        return self._telefone

    #Metodo set para telefone
    def set_telefone(self, telefone):
        self._telefone = telefone
