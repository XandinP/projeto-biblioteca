from prettytable import PrettyTable
from db.db_connect import ConnectDb
from models.pessoa import Pessoa
import cx_Oracle


class PessoaRepository: 
    def __init__(self, db: ConnectDb) -> None:
        self.db = db
        pass
    
    
    def inserir_no_banco(self, query): 
        self.db.cursor.execute(query)
        self.db.conexao.commit() 
        pass
    def inserir_pessoa(self, pessoa: Pessoa):
        query = f"insert into pessoas(cpf, nome) values ('{pessoa.cpf}', '{pessoa.nome}')"
        self.db.cursor.execute(query)
        self.db.conexao.commit() 
        pass

    def listar_pessoas(self):
        query = "select cpf, nome from pessoas"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
 
        table = PrettyTable(["CPF", "NOME"])
        for row in rows:
            table.add_row(row)
            
        return table
        
    def procurar_pessoa_por_cpf(self, cpf: str):
        query = f"select cpf, nome from pessoas where cpf = '{cpf}'"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchone()
    
    def atualizar_pessoa(self, cpf, nome):
        
        try:
            query = f"update pessoas set nome = '{nome}' where cpf = '{cpf}'"
            self.db.cursor.execute(query)
            self.db.conexao.commit()
        except cx_Oracle.Error as error:
            print(error)
        pass
    

    def deletar_pessoa(self, cpf):
        query = f"delete from pessoas where cpf = '{cpf}'"
        self.db.cursor.execute(query)
        self.db.conexao.commit()
        pass
        
        