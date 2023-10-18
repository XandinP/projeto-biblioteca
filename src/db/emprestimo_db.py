from prettytable import PrettyTable
from db.db_connect import ConnectDb
from models.aluno import Aluno
from models.emprestimo import Emprestimo
from models.livro import Livro
import cx_Oracle

class EmprestimoDb:
    def __init__(self, db:ConnectDb) -> None:
        self.db = db
        pass
    
    
    def inserir_no_banco(self, query): 
        self.db.cursor.execute(query)
        self.db.conexao.commit() 
        pass
    
    
    def inserir_livro(self, livro: Livro):
        query = f"insert into livro(isbn, titulo, autor, ano, categoria, numdecopias) values  ('{livro.isbn}', '{livro.titulo}','{livro.autor}', '{livro.ano}','{livro.categoria}', '{livro.num_copia_disponiveis}')"
        self.db.cursor.execute(query)
        self.db.conexao.commit() 
        pass
    
    
    def inserir_emprestimo(self, emprestimo: Emprestimo):
        query = f"insert into emprestimo(idemprestimo, dataemprestimo, datadevolucao, isbn, numid) values   ('{emprestimo.id_emprestimo}', '{emprestimo.data_emprestimo}','{emprestimo.data_devolucao}', '{emprestimo.livro}','{emprestimo.aluno}')"
        self.db.cursor.execute(query)
        self.db.conexao.commit() 
        pass
        
    def inserir_aluno(self, aluno: Aluno):
        query = f"insert into aluno(numid, nome, turma) values ('{aluno.num_id}', '{aluno.nome}','{aluno.turma}')"
        self.db.cursor.execute(query)
        self.db.conexao.commit()         
        pass
    
    def remover_livro(self, isbn ):
        query = f"delete from livro where isbn = '{isbn}'"
        self.db.cursor.execute(query)
        self.db.conexao.commit()
        pass
    
    def remover_aluno(self, num_id):
        query = f"delete from aluno where numid = '{num_id}'"
        self.db.cursor.execute(query)
        self.db.conexao.commit()
        pass
    
    def remover_emprestimo(self, id_emprestimo):
        query = f"delete from emprestimo where idemprestimo = '{id_emprestimo}'"
        self.db.cursor.execute(query)
        self.db.conexao.commit()
        pass
    
    def atualizar_aluno(self, num_id, nome, turma):
        
        try:
            query = f"update pessoas set nome = '{nome}', turma = '{turma}' where numid = '{num_id}'"
            self.db.cursor.execute(query)
            self.db.conexao.commit()
        except cx_Oracle.Error as error:
            print(error)
        pass
    
    
    def verificar_disponibilidade_livro(self, isbn):
        query = f"select count (*) from emprestimo where isbn = '{isbn}' and datadevolucao is null"
        self.db.cursor.execute(query)
        resultado = self.db.cursor.fetchone()
        try:
            if resultado > 0:
                return f"O livro com ISBN {isbn} esta emprestado."
            else:
                 return f"O livro com ISBN {isbn} esta disponivel para emprestimo."
        except Exception as e:
            return f"Ocorreu um erro ao verificar a disponibilidade do livro: {str(e)}"
    
    def listar_livros(self):
        query = "select isbn, titulo, autor, ano, categoria, numcopiasdisponiveis from livro"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
 
        table = PrettyTable(["ISBN", "TITULO", "AUTOR", "ANO","CATEGORIA", "NUMERO DE COPIAS"])
        for row in rows:
            table.add_row(row)
            
        return table
    

    def listar_alunos(self):
        query = "select numid, nome, turma, from aluno"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
 
        table = PrettyTable(["IDALUNO", "NOME", "TURMA"])
        for row in rows:
            table.add_row(row)
            
        return table
    
            
    def listar_emprestimo(self):
        query = "select idemprestimo, isbn, numid, dataemprestimo, datadevolucao from emprestimo"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
 
        table = PrettyTable(["ID DO EMPRESTIMO", "ISBN", "NUMID", "DATA DO EMPRESTIMO", "DATA DA DEVOLUCAO"])
        for row in rows:
            table.add_row(row)
            
        return table         