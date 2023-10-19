import os
from rich import print
from rich.prompt import Prompt

from db.database_manager import DatabaseManager
from utils.menus import Menus


class Relatorios:
    def __init__(self, db: DatabaseManager) -> None:
        self.db = db
        self.menu = Menus(db)

    def showMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
        
        ## Livros por categoria =  agrupamento
        ## Emprestimos = juncao de tabelas
        menu = """
[bold yellow]RELATORIOS[/bold yellow]
[bold cyan]1.[/bold cyan] Relatorio livros por categoria
[bold cyan]2.[/bold cyan] Relatorio de Emprestimos
[bold cyan]3.[/bold cyan] Relatorio de Alunos
[bold cyan]4.[/bold cyan] Relatorio de Livros
[bold cyan]5.[/bold cyan] Voltar ao menu
        """

        while True:
            print(menu)
            opt = int(Prompt.ask("Selecione uma opcao"))

            if opt == 1:
                print("\033c", end="")
                self.relatorioLivrosPorCategoria()
            elif opt == 2:
                print("\033c", end="")
                self.relatorioEmprestimos()
            elif opt == 3:
                print("\033c", end="")
                self.relatorioAlunos()
            elif opt == 4:
                print("\033c", end="")
                self.relatorioLivros()
            elif opt == 5:
                break
            else:
                print("Opcao invalida, tente novamente")

    def relatorioAlunos(self):
        query = """
            select * from aluno
        """

        alunos = self.db.readAll(query)
        self.menu.showAsTable(alunos)
        pass

    def relatorioLivros(self):
        query = """
            select * from livro
        """
        livros = self.db.readAll(query)
        self.menu.showAsTable(livros)
        pass
    
    #lista a quantidade de livros por categoria
    def relatorioLivrosPorCategoria(self):
        query = """
            select categoria, count(*) as num_livros from livro group by categoria
        """
        
        livros = self.db.readAll(query)
        self.menu.showAsTable(livros)
        
    #lista os emprestimos mostrando o titulo do livro e o aluno
    def relatorioEmprestimos(self):
        query = """
            select e.idemprestimo, e.dataemprestimo, e.datadevolucao, a.nome as aluno, l.titulo as livro
            from emprestimo e
            join aluno a on e.id_aluno = a.id
            join livro l on e.isbn = l.isbn
        """

        emprestimos = self.db.readAll(query)
        self.menu.showAsTable(emprestimos)
