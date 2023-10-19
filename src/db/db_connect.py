import cx_Oracle
from prettytable import PrettyTable

from pandas import DataFrame
class ConnectDb:
    
    def __init__(self, can_write:bool=False) -> None:
        self.can_write =can_write
        self.usuario = "system"
        self.senha = "32256029"
        self.dsn = "localhost/xe"
        pass
    
    def criar_conexao(self):
        print("criando conexao")
        self.conexao = cx_Oracle.connect(user= self.usuario, password = self.senha, dsn = self.dsn)
        self.cursor = self.conexao.cursor()
       
    
    def ping(self):
        self.cursor.execute("select sysdate from dual")
        print(self.cursor.fetchall())
        
    def write(self, query:str):
        if not self.can_write:
            raise Exception('Nao e possivel escrever usando esta conexao')
        self.cursor.execute(query)
        self.conexao.commit()
     
     
    ## retorna a lista sem formatacao em prettytable
    def readAll(self, query): ## le dados
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    ## retorna um unico valor sem formatacao em prettytable
    def readOne(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    ## retorna a lista formatada
    def readAll_toTable(self, query):
        rows = self.readAll(query)
        column_names = [desc[0].upper() for desc in self.cursor.description]

        table = PrettyTable(column_names)
        for row in rows:
            table.add_row(row)

        return table
    
    ## retorna um valor formatado
    def readOne_toTable(self, query):
        rows = self.readOne(query)
        column_names = [desc[0].upper() for desc in self.cursor.description]

        table = PrettyTable(column_names)
        for row in rows:
            table.add_row(row)

        return table
        

    def delete(self, query:str):
        if not self.can_write:
            raise Exception('Nao e possivel escrever usando esta conexao')
        self.cursor.execute(query)
        self.conexao.commit()
    
    def pegar_contagem(self, tabela):
        self.cursor.execute(f"select count(*) from {tabela}")
        return self.cursor.fetchone()[0]
        
    def fechar_conexao(self):
        print("fechando conexao")
        self.cursor.close()
        self.conexao.close()
        
    
    def verificar_disponibilidade_livro(self, isbn):
        query = f"select count (*) from emprestimo where isbn = '{isbn}' and datadevolucao is null"
        self.db.cursor.execute(query)
        resultado = self.db.cursor.fetchone()[0]
        try:
            if resultado > 0:
                return f"O livro com ISBN {isbn} esta emprestado."
            else:
                 return f"O livro com ISBN {isbn} esta disponivel para emprestimo."
        except Exception as e:
            return f"Ocorreu um erro ao verificar a disponibilidade do livro: {str(e)}"
    