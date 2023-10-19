from db.db_connect import ConnectDb
from utils import menu

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_produtos = menu.QUERY_COUNT.format(tabela="alunos")
        self.qry_total_clientes = menu.QUERY_COUNT.format(tabela="emprestimo")
        self.qry_total_fornecedores = menu.QUERY_COUNT.format(tabela="livro")
        
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Alexandre P.Costa"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConnectDb()
        oracle.criar_conexao()
        # Retorna o total de registros computado pela query
        return oracle.readOne_toTable(self.qry_total_produtos)["total_produtos"].values[0]

    def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConnectDb()
        oracle.criar_conexao()
        # Retorna o total de registros computado pela query
        return oracle.readOne_toTable(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConnectDb()
        oracle.criar_conexao()
        # Retorna o total de registros computado pela query
        return oracle.readOne_toTable(self.qry_total_fornecedores)["total_fornecedores"].values[0]

    def get_total_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConnectDb()
        oracle.criar_conexao()
        # Retorna o total de registros computado pela query
        return oracle.readOne_toTable(self.qry_total_pedidos)["total_pedidos"].values[0]

    def get_total_itens_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConnectDb()
        oracle.criar_conexao()
        # Retorna o total de registros computado pela query
        return oracle.readOne_toTable(self.qry_total_itens_pedido)["total_itens_pedido"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:         {str(self.get_total_produtos()).rjust(5)}
        #      2 - CLIENTES:         {str(self.get_total_clientes()).rjust(5)}
        #      3 - FORNECEDORES:     {str(self.get_total_fornecedores()).rjust(5)}
        #      4 - PEDIDOS:          {str(self.get_total_pedidos()).rjust(5)}
        #      5 - ITENS DE PEDIDOS: {str(self.get_total_itens_pedidos()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """