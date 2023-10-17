import cx_Oracle

class ConnectDb:
    
    def __init__(self) -> None:
        self.usuario = "system"
        self.senha = "32256029"
        self.dsn = "localhost/xe"
        pass
    
    def criar_conexao(self):
        print("criando conexao")
        self.conexao = cx_Oracle.connect(user= self.usuario, password = self.senha, dsn = self.dsn)
        self.cursor = self.conexao.cursor()
        pass
    
    def ping(self):
        self.cursor.execute("select sysdate from dual")
        print(self.cursor.fetchall())
        
    def write(self, query): ## manipula dado, insere, remove, atualiza
        pass
     
    def read(self, query): ## le dados
        pass
        
    def fechar_conexao(self):
        print("fechando conexao")
        self.cursor.close()
        self.conexao.close()