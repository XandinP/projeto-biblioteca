
from db.db_connect import ConnectDb
import cx_Oracle

class EmprestimoDb:
    def __init__(self, db:ConnectDb) -> None:
        self.db = db
        pass
    
    
    def atualizar_aluno(self, num_id, nome, turma):
        
        try:
            query = f"update aluno set nome = '{nome}', turma = '{turma}' where numid = '{num_id}'"
            self.db.cursor.execute(query)
            self.db.conexao.commit()
        except cx_Oracle.Error as error:
            print(error)
        pass

    def atualizar_livro(self, isbn, titulo, ano, autor, categoria, numcopiasdisponiveis):
        
        try:
            query = f"update livro set titulo = '{titulo}', ano = '{ano}', autor = '{autor}', categoria = '{categoria}', numcopiasdisponiveis = '{numcopiasdisponiveis}' where isbn = '{isbn}'"
            self.db.cursor.execute(query)
            self.db.conexao.commit()
        except cx_Oracle.Error as error:
            print(error)
        pass
    
    def atualizar_emprestimo(self, idemprestimo , dataemprestimo , datadevolucao , isbn , numid):
        
        try:
            query = f"update emprestimo set dataemprestimo = '{dataemprestimo}',datadevolucao = '{datadevolucao}', isbn = '{isbn}', numid = '{numid}' where idemprestimo = '{idemprestimo}'"
            self.db.cursor.execute(query)
            self.db.conexao.commit()
        except cx_Oracle.Error as error:
            print(error)
        pass
            