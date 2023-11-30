import os
from db.database_manager import DatabaseManager
from db.mongo_manager import MongoManager
from services.atualizar_registros import AtualizarRegistros
from services.inserir_registros import InserirRegistros
from services.relatorios import Relatorios
from rich.prompt import Prompt
from services.remover_registros import RemoverRegistros
from sync import Sync
from utils.menus import Menus

oracle_db = DatabaseManager()
oracle_db.createConnection()

mongo_db = MongoManager()
mongo_db.init_conn()

menus = Menus(oracle_db)


while True: 
    menus.displayInitMenu()
    opt = menus.chooseDbMenu()

    # oracle
    if opt == 1:

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            
            opt = menus.displayMainMenu()
            
            if opt == 1: 
                relatorios = Relatorios(oracle_db)
                relatorios.showMenu()
                menus.confirmar()
            elif opt == 2:
                inserirRegistros = InserirRegistros(oracle_db)
                inserirRegistros.showMenu()
                menus.confirmar()
                
            elif opt == 3:
                removerRegistros = RemoverRegistros(oracle_db)
                removerRegistros.showMenu()
                menus.confirmar()
                
            elif opt == 4:
                atualizarRegistros = AtualizarRegistros(oracle_db)
                atualizarRegistros.showMenu()
                menus.confirmar()
                
            elif opt == 5:
                print("Saindo")
                break
            else: 
                print("Opcao invalida, tente novamente")
    # mongo
    elif opt == 2:
        mongoOpt = menus.mongoMenu()
        if mongoOpt == 1:
            alunos = mongo_db.read_all_alunos()
            mongo_db.show_as_table(alunos)
            menus.confirmar()
        elif mongoOpt == 2:
            livros = mongo_db.read_all_livros()
            mongo_db.show_as_table(livros)
            menus.confirmar()
        elif mongoOpt == 3:
            emprestimos = mongo_db.read_all_emprestimos()
            mongo_db.show_as_table(emprestimos)
            menus.confirmar()
        elif mongoOpt == 4:
            break
    # sincronizar dados
    elif opt == 3:
        sync = Sync(mongo=mongo_db, oracle_db= oracle_db)
        sync.sinc(True)
    # sair
    elif opt == 4:
        break


print("Finalizando aplicacao")