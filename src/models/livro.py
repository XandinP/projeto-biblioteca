class Livro:
    def __init__(self,isbn , titulo, autor, ano, categoria, num_copia_disponiveis) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.num_copia_disponiveis = num_copia_disponiveis
        pass
    def to_string(self):
        return f'isbn: {self.isbn}, titulo: {self.titulo}, autor: {self.autor}, ano: {self.ano}, categoria: {self.categoria}, numdecopias: {self.num_copia_disponiveis}'