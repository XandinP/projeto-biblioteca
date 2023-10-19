from db.database_manager import DatabaseManager
from rich import print
from rich.prompt import Prompt, Confirm
import os

from utils.menus import Menus

class RemoverRegistros:
    def __init__(self, db: DatabaseManager) -> None:
        self.db = db
        self.menu = Menus(db)
        
    def showMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
        menu =  """
[bold yellow]DELETAR REGISTROS [/bold yellow]
[bold cyan]1.[/bold cyan] Emprestimos
[bold cyan]2.[/bold cyan] Livros
[bold cyan]3.[/bold cyan] Alunos
[bold cyan]4.[/bold cyan] Voltar ao menu
        """
        
        while True:
            print(menu)
            opt = int(Prompt.ask("Selecione uma opcao"))
            
            if opt == 1:
                self.deleteEmprestimo()
            elif opt == 2:
                self.deleteLivro()
            elif opt == 3:
                self.deleteAluno()
            elif opt == 4:
                break
            else:
                print("Opcao invalida, tente novamente")
        pass
    
    def deleteEmprestimo(self):
        emprestimos = self.db.readAll("select * from emprestimo")
        self.menu.showAsTable(emprestimos)
        while True:
            id = int(Prompt.ask("Informe o id do emprestimo a ser deletado"))
            confirmacao = Confirm.ask(f"Tem certeza que deseja deletar o emprestimo {id}")
            
            if confirmacao:
                self.db.delete(f"delete from emprestimo where idemprestimo = {id}")
            confirmacao = Confirm.ask("deseja deletar outro emprestimo ?")
            if not confirmacao:
                print("\033c", end="")
                break
                        
    def deleteLivro(self):
        livros = self.db.readAll("select * from livro")
        self.menu.showAsTable(livros)
        
        while True:
            isbn = Prompt.ask("Informe o isbn do livro a ser deletado")
            
            existeEmprestimo = self.validaSeExisteEmprestimo(isbn=isbn)
            
            if existeEmprestimo:
                print("Existem emprestimos com esse livro, delete-os antes de deletar o livro")                  
            else:
                confirmacao = Confirm.ask(f"Tem certeza que deseja deletar o livro de isbn {isbn}?")
                if confirmacao:
                    self.db.delete(f"delete from livro where isbn = '{isbn}'")
            confirmacao = Confirm.ask("deseja deletar outro livro ?")
            if not confirmacao:
                print("\033c", end="")
                break
                    
            
            
    def deleteAluno(self):
        livros = self.db.readAll("select * from aluno")
        self.menu.showAsTable(livros)
        
        while True:
            idAluno = int(Prompt.ask("Informe o id do aluno a ser deletado"))
            
            existeEmprestimo = self.validaSeExisteEmprestimo(idAluno=idAluno)
            
            if existeEmprestimo:
                print("Existem emprestimos com esse aluno, delete-os antes de deletar o aluno")                  
            else:
                confirmacao = Confirm.ask(f"Tem certeza que deseja deletar o aluno de id {idAluno}?")
                if confirmacao:
                    self.db.delete(f"delete from aluno where id = {idAluno}")
            confirmacao = Confirm.ask("deseja deletar outro aluno ?")
            if not confirmacao:
                print("\033c", end="")
                break
            
        
    def validaSeExisteEmprestimo(self, isbn=None, idAluno=None):
        ## se estiver passando aluno, busca por aluno
        if idAluno != None and isbn == None:
           emprestimos = self.db.readAll(f"select * from emprestimo where id_aluno = {idAluno}")
        
        ## se estiver passando isbn, busca por isbn
        elif isbn != None and idAluno == None:
            emprestimos = self.db.readAll(f"select * from emprestimo where isbn = '{isbn}'")
        else:
            return False
        
        if emprestimos == None or emprestimos == []:
               return False
        return True