from db.db_connect import ConnectDb
from db.emprestimo_db import EmprestimoDb
from models.aluno import Aluno
from models.emprestimo import Emprestimo
from models.livro import Livro

db = ConnectDb(can_write=True)
db.criar_conexao()
geral  = EmprestimoDb(db)

# livro =  Livro('213421244', 'O Guia do Programador', 'Carlos Pereira', 2021, 'Tecnologia', 15)
# geral.inserir_livro(livro)

# status_livro = geral.verificar_disponibilidade_livro('9785678901234')
# print(status_livro)

#clicou em deletar

## deletando registro
print(db.readAll_toTable("select * from emprestimo"))

def remover_aluno():
    while True:
        ## lista tabela selecionada
        print(db.readAll_toTable("select * from aluno"))

        # digite o id a deletar
        id_selecionado = input("qual id deletar")
        
        opt = input(f"Tem certeza que deseja deletar o id {id_selecionado}? S/N")
        
        if opt in ['S', 's']:
            ## verifica se existe FK
            idemprestimo = db.readAll(f"select idemprestimo from emprestimo where numid = {id_selecionado}")
            if len(idemprestimo) > 0:
                ## nao tem como opcao
                input(f'Nao e possivel deletar pois ha registros na tabela emprestimos com o aluno {id_selecionado}\nPressione enter para voltar ao menu')
                #break ## quebrar loop
                
                ## opcao deletar filho
                opt = input(f'Existem registros na tabela emprestimos com o aluno {id_selecionado}, deseja deleta-los junto? S/N')
                
                if opt in ['S', 's']:
                    for (id_value,) in idemprestimo:
                        db.delete(f'delete from emprestimo where numid = {id_value}') ## deleta registros na table de relacao

                    db.delete(f'delete from aluno where numid = {id_selecionado}') ## deleta registro selecionado.
                else:
                    break
            
            opt = input(f'Deseja excluir mais algum registro?\n S/N')
            if opt in ['S', 's']:
                continue
            else:
                break ## volta ao menu
        else:
            print('voltando ao menu')
            #volta ao menu
            break ## volta ao menu
        
    
    chamar_menu()
        
    
print("Tabela aluno") 
print(db.readAll_toTable("select * from aluno"))
print("Tabela emprestimo")
print(db.readAll_toTable("select * from emprestimo"))
