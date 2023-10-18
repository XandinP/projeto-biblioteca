from models.aluno import Aluno
from models.livro import Livro
class Emprestimo:
   def __init__(self, id_emprestimo, data_emprestimo, data_devolucao) -> None:
       self.id_emprestimo = id_emprestimo
       self.data_emprestimo = data_emprestimo
       self.data_devolucao = data_devolucao
       self.aluno:Aluno
       self.livro:Livro
       pass
   def to_string(self):
       return f'id do emprestimo: {self.id_emprestimo}, data do emprestimo: {self.data_emprestimo}, data de devolucao: {self.data_devolucao},id do aluno:{self.aluno.num_id}, isbn livro: {self.livro.isbn} '