import sqlite3 as sql

class TransactionObject():
    def __init__(self, database="clientes.db"):
        self.database = database
        self.conn = None
        self.cur = None
        self.connected = False

    def connect(self):
        """Estabelece a conexão com o banco de dados"""
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.connected = False

    def execute(self, query, parms=None):
        """Executa um comando SQL"""
        if not self.connected:
            raise ConnectionError("Não há conexão ativa com o banco de dados.")
        if parms is None:
            self.cur.execute(query)
        else:
            self.cur.execute(query, parms)

    def fetchall(self):
        """Retorna todos os resultados da última execução"""
        return self.cur.fetchall()

    def persist(self):
        """Faz o commit das mudanças"""
        if self.connected:
            self.conn.commit()
        else:
            raise ConnectionError("Não há conexão ativa para persistir os dados.")

def initDB():
    """Inicializa o banco de dados com a tabela necessária"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
    finally:
        trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    """Insere um novo cliente na tabela"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
    finally:
        trans.disconnect()

def view():
    """Retorna todos os clientes da tabela"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        return rows
    finally:
        trans.disconnect()

def search(nome="", sobrenome="", email="", cpf=""):
    """Busca clientes com base nos parâmetros fornecidos"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        return rows
    finally:
        trans.disconnect()

def delete(id):
    """Deleta um cliente com base no ID fornecido"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
        trans.persist()
    finally:
        trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    """Atualiza as informações de um cliente com base no ID"""
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?", (nome, sobrenome, email, cpf, id))
        trans.persist()
    finally:
        trans.disconnect()

# Inicializar o banco de dados ao carregar o módulo
initDB()
