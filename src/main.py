import os
from db.database_manager import DatabaseManager
from services.atualizar_registros import AtualizarRegistros
from services.inserir_registros import InserirRegistros
from services.relatorios import Relatorios
from rich.prompt import Prompt
from services.remover_registros import RemoverRegistros
from utils.menus import Menus

db = DatabaseManager()
db.createConnection()

menus = Menus(db)


menus.displayInitMenu()

while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    opt = menus.displayMainMenu()
    
    if opt == 1: 
        relatorios = Relatorios(db)
        relatorios.showMenu()
        menus.confirmar()
    elif opt == 2:
        inserirRegistros = InserirRegistros(db)
        inserirRegistros.showMenu()
        menus.confirmar()
        
    elif opt == 3:
        removerRegistros = RemoverRegistros(db)
        removerRegistros.showMenu()
        menus.confirmar()
        
    elif opt == 4:
        atualizarRegistros = AtualizarRegistros(db)
        atualizarRegistros.showMenu()
        menus.confirmar()
        
    elif opt == 5:
        print("Saindo")
        break
    else: 
        print("Opcao invalida, tente novamente")


print("Finalizando aplicacao")
        
    
    
