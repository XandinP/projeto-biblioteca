from pymongo import MongoClient
from tabulate import tabulate 
from models.aluno import Aluno
from models.emprestimo import Emprestimo

from models.livro import Livro


class MongoManager:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 27017
        self.db_name = "Projeto"

        self.client = None
        self.database = None

        self.aluno_coll = None
        self.livro_coll = None
        self.emprestimo_coll = None 

        self.init_conn()

        pass

    
    def init_conn(self):
        self.client = MongoClient(self.host, self.port)
        self.database = self.client[self.db_name]
        pass


    def read_all_livros(self):
        livro_docs = self.database.livros.find()
        livros = [Livro(isbn=doc.get('isbn'), titulo=doc.get('titulo'), autor=doc.get('autor'), ano=doc.get('ano'), categoria=doc.get('categoria'), copiasDisponiveis=doc.get('copiasDisponiveis')) for doc in livro_docs]
        return livros
    
    def read_all_emprestimos(self):
        emprestimo_docs = self.database.emprestimos.find()
        emprestimos = [Emprestimo(idEmprestimo=doc.get('idEmprestimo'), dataEmprestimo=doc.get('dataEmprestimo'), dataDevolucao=doc.get('dataDevolucao'), isbn=doc.get('isbn'), alunoId=doc.get('alunoId')) for doc in emprestimo_docs]
        return emprestimos
    
    def read_all_alunos(self):
        aluno_docs = self.database.alunos.find()
        alunos = [Aluno(id=doc.get('id'), turma=doc.get('turma'), nome=doc.get('nome')) for doc in aluno_docs]
        return alunos
    
    def show_as_table(self, values):
        values_dict = [value.__dict__ for value in values]
        print(tabulate(values_dict, headers="keys", tablefmt="heavy_grid"))