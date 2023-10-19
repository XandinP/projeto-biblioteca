class Livro:
    def __init__(self, isbn=None, titulo=None, autor=None, ano=None, categoria=None, copiasDisponiveis=None) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.copiasDisponiveis = copiasDisponiveis
        pass
    