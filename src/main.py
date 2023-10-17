
from random import randint
from db.db_connect import ConnectDb
from db.pessoa_repository import PessoaRepository
from models.pessoa import Pessoa



db = ConnectDb()
db.criar_conexao()
pessoaRepository = PessoaRepository(db)

## create



value = randint(111111111, 999999999)
value1 = f"{value}"
pessoa = Pessoa("Alexandre2", value1)
pessoaRepository.inserir_pessoa(pessoa)


## list all
pessoas = pessoaRepository.listar_pessoas()

print(pessoas)



## list by
print(f"Listando \n {pessoaRepository.procurar_pessoa_por_cpf(value1)}")


##update
pessoaRepository.atualizar_pessoa(value1, "Rodrigo Pinheiro dos Santos")
print(f"Pessoa encontrada: {pessoaRepository.procurar_pessoa_por_cpf(value1)}")


## delete
# pessoaRepository.deletar_pessoa(value1)
# print(f"Devia estar None: {pessoaRepository.procurar_pessoa_por_cpf(value1)}")








db.fechar_conexao() ## fecha conexao qnd terminar o arquivo
