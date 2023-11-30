from db.database_manager import DatabaseManager
from db.mongo_manager import MongoManager

from models.aluno import Aluno
from models.livro import Livro
from models.emprestimo import Emprestimo

class Sync:
    def __init__(self, oracle_db, mongo: MongoManager) -> None:
        self.oracle_db = oracle_db
        self.mongo = mongo

        pass

    def sync(self, drop_if_exists: bool = False):
        emprestimos_oracle = self.oracle_db.readAll("select * from emprestimo")
        emprestimos = [Emprestimo(idEmprestimo=row[0], dataEmprestimo=row[1], dataDevolucao=row[2], isbn=row[3], alunoId=row[4]) for row in emprestimos_oracle]
   
        alunos_oracle = self.oracle_db.readAll("select * from aluno")
        alunos = [Aluno(id=row[0], turma=row[1], nome=row[2]) for row in alunos_oracle]

        livros_oracle = self.oracle_db.readAll("select * from livro")
        livros = [Livro(isbn=row[0], titulo=row[1], autor=row[2], ano=row[3], categoria=row[4], copiasDisponiveis=row[5]) for row in livros_oracle]

        if drop_if_exists:
            self.drop_colls()
        self.create_colls()

        ## cria dicionarios dos dados que pegamos do mysql
        aluno_dicts = [aluno.__dict__ for aluno in alunos]
        livro_dicts = [livro.__dict__ for livro in livros]
        emprestimo_dicts = [emprestimo.__dict__ for emprestimo in emprestimos]


        ## insere eles no mongo
        self.mongo.aluno_coll.insert_many(aluno_dicts)
        self.mongo.livro_coll.insert_many(livro_dicts)
        self.mongo.emprestimo_coll.insert_many(emprestimo_dicts)
        pass
    
    def drop_colls(self):
        self.mongo.database.alunos.drop()
        self.mongo.database.livros.drop()
        self.mongo.database.emprestimos.drop()
        pass

    def create_colls(self):
        self.mongo.aluno_coll = self.mongo.database["alunos"]
        self.mongo.livro_coll = self.mongo.database["livros"]
        self.mongo.emprestimo_coll = self.mongo.database["emprestimos"]
        pass


## conectando ao sql
oracle_db = DatabaseManager()
oracle_db.createConnection()

mongo = MongoManager()
mongo.init_conn()

sync = Sync(oracle_db, mongo)
sync.sync(True)
