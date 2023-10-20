import os
from db.database_manager import DatabaseManager
from rich import print
from rich.prompt import Prompt, Confirm
from models.aluno import Aluno
from models.emprestimo import Emprestimo
from models.livro import Livro

from utils.menus import Menus

class AtualizarRegistros:
    def __init__(self, db: DatabaseManager) -> None:
        self.db = db
        self.menu = Menus(db)
        

    def showMenu(self):
        os.system("cls" if os.name == "nt" else "clear")

        menu = """
[bold yellow]
====================================
==       ATUALIZAR REGISTROS      ==
====================================
[/bold yellow]

[bold cyan]1.[/bold cyan] Emprestimos (Devolver livro)
[bold cyan]2.[/bold cyan] Livros
[bold cyan]3.[/bold cyan] Alunos
[bold cyan]4.[/bold cyan] Voltar ao menu

        """
        
        while True:
            print(menu)
            opt = int(Prompt.ask("Selecione uma opcao"))
            
            if opt == 1:
                self.devolverLivro()
            elif opt == 2:
                self.updateLivro()
            elif opt == 3:
                self.updateAluno()
            elif opt == 4:
                break
            else:
                print("Opcao invalida, tente novamente")
        pass
    
    def devolverLivro(self):
        while True:
            emprestimos = self.db.readAll("select * from emprestimo")
            self.menu.showAsTable(emprestimos)
            idEmprestimo = int(Prompt.ask("Informe o id do emprestimo a ser devolvido"))
            
            emprestimoSelecionado = None
            for emprestimo in emprestimos:
                if emprestimo[0] == idEmprestimo:
                    emprestimoSelecionado = Emprestimo(*emprestimo)
            
            if emprestimoSelecionado:
                ## devolve livre
                query = f"update emprestimo set datadevolucao = SYSDATE where idemprestimo = {idEmprestimo}"
                self.db.update(query)
                
                
                ## adiciona copia do livro disponivel
                query = f"update livro set copias_disponiveis = copias_disponiveis + 1 where isbn = {emprestimoSelecionado.isbn}"
                self.db.update(query)
                atualizarOutro = Confirm.ask("Deseja devolver mais algum emprestimo?")
                print("\033c", end="")
                if not atualizarOutro:
                    print("\033c", end="")
                    break
                
            else:
                print("\033c", end="")
                print("Emprestimo nao encontrado")
        pass

    def updateLivro(self):
        while True:
            livros = self.db.readAll("select * from livro")
            self.menu.showAsTable(livros)
            isbn = Prompt.ask("Informe o isbn do livro a ser atualizado")
            
            livroSelecionado = None
            for livro in livros:
                if livro[0] == isbn:
                    livroSelecionado = Livro(*livro)
            
            if livroSelecionado:
                print("Deixe em branco os campos que nao quiser atualizar")
                novoTitulo = Prompt.ask("Novo titulo", default=livroSelecionado.titulo)
                novoAutor = Prompt.ask("Novo autor", default=livroSelecionado.autor)
                novoAno = Prompt.ask("Novo ano", default=str(livroSelecionado.ano))
                novaCategoria = Prompt.ask("Nova categoria", default=livroSelecionado.categoria)
                novaQtdCopiasDisponiveis = Prompt.ask("Nova Quantidade de copias disponiveis", default=str(livroSelecionado.copiasDisponiveis))
                
                livro = Livro(isbn, novoTitulo, novoAutor, int(novoAno), novaCategoria, novaQtdCopiasDisponiveis)
                
            
                
                query = f"""
                    update livro set titulo = '{livro.titulo}', autor = '{livro.autor}', ano = {livro.ano}, categoria = '{livro.categoria}', copias_disponiveis = {livro.copiasDisponiveis}
                    where isbn = '{livro.isbn}'
                """
        
                self.db.update(query)
                
                livro = self.db.readOne(f"select * from livro where isbn = '{livro.isbn}'")
                print("Livro atualizado:")
                self.menu.showAsTable(livro)
                atualizarOutro = Confirm.ask("Deseja atualizar mais algum livro?")
                print("\033c", end="")
                if not atualizarOutro:
                    print("\033c", end="")
                    break
                
            else:
                print("\033c", end="")
                print("Livro nao encontrado")
            
            
        pass
    
    def updateAluno(self):
        
        while True:
            alunos = self.db.readAll("select * from aluno")
            self.menu.showAsTable(alunos)
            idAluno = int(Prompt.ask("Informe o id do aluno a ser atualizado"))
            
            alunoSelecionado = None
            for aluno in alunos:
                if aluno[0] == idAluno:
                    alunoSelecionado = Aluno(*aluno)
            
            if alunoSelecionado:
                print("Deixe em branco os campos que nao quiser atualizar")
                novoNome = Prompt.ask("Novo nome", default=alunoSelecionado.nome)
                novaTurma = Prompt.ask("Nova turma", default=alunoSelecionado.turma)
                
                aluno = Aluno(idAluno, novaTurma, novoNome)
            
                
                query = f"""
                    update aluno set nome = '{aluno.nome}', turma = '{aluno.turma}'
                    where id = '{aluno.id}'
                """
        
                self.db.update(query)
                
                aluno = self.db.readOne(f"select * from aluno where id = '{aluno.id}'")
                print("Aluno atualizado:")
                self.menu.showAsTable(aluno)
                
                atualizarOutro = Confirm.ask("Deseja atualizar mais algum aluno?")
                print("\033c", end="")
                if not atualizarOutro:
                    print("\033c", end="")
                    break
                
            else:
                print("\033c", end="")
                print("Aluno nao encontrado")
        pass
