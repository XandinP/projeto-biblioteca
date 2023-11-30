import os
import time
from rich import print
from rich.prompt import Prompt
from tabulate import tabulate

class Menus:
    def __init__(self, db):
        self.db = db
        pass

    def chooseDbMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
[bold cyan] Escolha o tipo de banco de dados[/bold cyan]
[bold yellow]1.[/bold yellow] Relacional - Oracle
[bold yellow]2.[/bold yellow] Nao relacional - Mongo
[bold yellow]3.[/bold yellow] Sincronizar dados do oracle com o mongo
[bold yellow]4.[/bold yellow] Sair
"""
        )

        opcao = Prompt.ask("Escolha uma opcao")
        return int(opcao)
    
    def mongoMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
[bold yellow]1.[/bold yellow] Listar alunos
[bold yellow]2.[/bold yellow] Listar livros
[bold yellow]3.[/bold yellow] Listar emprestimos
[bold yellow]4.[/bold yellow] Sair
"""
        )

        opcao = Prompt.ask("Escolha uma opcao")
        return int(opcao)
    

    def displayInitMenu(self):
        countAlunos = self.db.getCount("aluno")
        countEmprestimos = self.db.getCount("emprestimo") 
        countLivros = self.db.getCount("livro")

        os.system("cls" if os.name == "nt" else "clear")

        print(
            f"""
[bold cyan]Gerenciamento de Biblioteca Escolar[/bold cyan]
Alunos: [bold yellow]{countAlunos}[/bold yellow]
Livros: [bold yellow]{countLivros}[/bold yellow]
Emprestimos: [bold yellow]{countEmprestimos}[/bold yellow]

Criado por: [italic]Alexandre de Paula Costa[/italic]
Disciplina: Banco de Dados 2023/2
Professor: Howard Roatti
"""
        )
        Prompt.ask("Pressione [bold yellow]ENTER[/bold yellow] para continuar")  
        print("\033c", end="")  # Comando para limpar o console

    
    def displayMainMenu(self):
        print(
        """
[bold cyan]1.[/bold cyan] Relatorios
[bold cyan]2.[/bold cyan] Inserir registros
[bold cyan]3.[/bold cyan] Remover registros
[bold cyan]4.[/bold cyan] Atualizar Registros
[bold cyan]5.[/bold cyan] Sair
        """
        )
        
        opcao = Prompt.ask("Escolha uma opcao")
        return int(opcao)
    

    def confirmar(self):
        return Prompt.ask("Pressione [bold yellow]ENTER[/bold yellow] para continuar")
    
    
    def showAsTable(self, rows):
        if not isinstance(rows, (list)):
            rows = [rows] 
            
        if rows:
            colunas = [desc[0] for desc in self.db.cursor.description]  
            tabela_formatada = tabulate(rows, headers=colunas, tablefmt="heavy_grid") 
            print(tabela_formatada)
        else:
            print("Nenhum resultado encontrado.")
        pass