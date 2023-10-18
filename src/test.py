from db.db_connect import ConnectDb
from db.emprestimo_db import EmprestimoDb
from models.aluno import Aluno
from models.emprestimo import Emprestimo
from models.livro import Livro

db = ConnectDb
db.criar_conexao

geral  = EmprestimoDb(db)
livro =  Livro('9785678901234', 'O Guia do Programador', 'Carlos Pereira', 2021, 'Tecnologia', 15)
geral.inserir_livro(livro)

status_livro = geral.verificar_disponibilidade_livro('9785678901234')
print(status_livro)
