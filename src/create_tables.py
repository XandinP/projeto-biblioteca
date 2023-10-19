from db.db_connect import ConnectDb

def criacao_tabela(query:str):
    list_of_commands = query.split(";")

    oracle = ConnectDb(can_write=True)
    oracle.criar_conexao()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("executado com sucesso")
            except Exception as e:
                print(e)

def criacao_registro(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = ConnectDb(can_write=True)
    oracle.criar_conexao()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("executado com sucesso")

def run():

    with open("sql/create_tables_biblioteca.sql", 'r', encoding="utf-8") as f:
        query_create = f.read()

    print("Criando tabelas ...")
    criacao_tabela(query=query_create)
    print("tabelas criadas com sucesso!")

    with open("sql/inserindo_dados_tabela.sql", 'r', encoding="utf-8") as f:
        query_generate_records = f.read()

    print("gerando registros")
    criacao_registro(query=query_generate_records)
    print("registros gerado com sucesso!")

if __name__ == '__main__':
    run()