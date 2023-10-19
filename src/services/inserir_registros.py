import os
from db.database_manager import DatabaseManager
from rich import print
from rich.prompt import Prompt, Confirm

from models.aluno import Aluno
from models.livro import Livro

class InserirRegistros:
    
    def __init__(self, db: DatabaseManager) -> None:
        self.db = db
        
    def showMenu(self):
        os.system("cls" if os.name == "nt" else "clear")

        menu = """
[bold yellow]INSERIR REGISTROS[/bold yellow]
[bold cyan]1.[/bold cyan] Emprestimos
[bold cyan]2.[/bold cyan] Livros
[bold cyan]3.[/bold cyan] Alunos
[bold cyan]4.[/bold cyan] Voltar ao menu
        """
        
        while True:
            print(menu)
            opt = int(Prompt.ask("Selecione uma opcao"))
            
            if opt == 1:
                self.insertEmprestimo()
            elif opt == 2:
                self.insertLivro()
            elif opt == 3:
                self.insertAluno()
            elif opt == 4:
                break
            else:
                print("Opcao invalida, tente novamente")
        pass
    
    def insertAluno(self):
        while True:
            nome = Prompt.ask("Nome do aluno")
            turma = Prompt.ask("Turma do aluno")
            
            aluno = Aluno(nome=nome,turma=turma)
            
            query = f"""
                insert into aluno (id, nome, turma) 
                values (ID_ALUNO_SEQ.nextval, '{aluno.nome}', '{aluno.turma}')
            """
            self.db.insert(query)
            
            inserirOutro = Confirm.ask("Deseja inserir mais algum aluno?")
            
            if not inserirOutro:
                break
            
    def insertLivro(self):
        while True:
            isbn = Prompt.ask("ISBN do livro")
            titulo = Prompt.ask("Titulo do livro")
            autor = Prompt.ask("Autor do livro")
            ano = Prompt.ask("Ano de lancamento do livro")
            categoria = Prompt.ask("Categoria do livro")
            copiasDisponiveis = Prompt.ask("Copias disponiveis do livro")
            
            livro = Livro(isbn, titulo, autor, ano, categoria, copiasDisponiveis)
            
            query = f"""
                insert into livro
                values ('{livro.isbn}', '{livro.titulo}', '{livro.autor}', {livro.ano}, '{livro.categoria}', {livro.copiasDisponiveis})
            """
            self.db.insert(query)
            
            inserirOutro = Confirm.ask("Deseja inserir mais algum livro?")
            
            if not inserirOutro:
                break
    
    def insertEmprestimo(self):
        while True:
            isbn = Prompt.ask("ISBN do livro a ser emprestado")
            if self.validaLivro(isbn):
                idAluno = Prompt.ask("Id do aluno que vai emprestar")
                
                if self.validaAluno(idAluno):
                    query = f"""
                        insert into emprestimo (idemprestimo, isbn, id_aluno)
                        values (ID_EMPRESTIMO_SEQ.nextval, '{isbn}', {idAluno})
                    """
                    
                    self.db.insert(query)
                    self.db.update(f"update livro set copias_disponiveis = copias_disponiveis - 1 where isbn = '{isbn}' ")
                    inserirOutro = Confirm.ask("Deseja inserir mais algum emprestimo?")
                    
                    if not inserirOutro:
                        break
                else:
                    escolherOutro = Confirm.ask("O aluno escolhido nao existe, deseja escolher outro?")
                    if not escolherOutro:
                        break                
            else:
                escolherOutro = Confirm.ask("O livro escolhido nao possui copias ou nao existe no momento, deseja escolher outro?")
                if not escolherOutro:
                    break
                else:
                    print("Voltando ao menu.") 
        
    def validaLivro(self, isbn: str):
        copiasDisponiveis = self.db.readOne(f"select copias_disponiveis from livro where isbn = '{isbn}'")
        
        if copiasDisponiveis == None:
            return False
        elif copiasDisponiveis == 0:
            return False
        
        return True

    def validaAluno(self, idAluno: int):
        aluno = self.db.readOne(f"select * from aluno where id = {idAluno} ")
        
        if aluno == None:
            return False
        return True
        
        
        
        
            
    