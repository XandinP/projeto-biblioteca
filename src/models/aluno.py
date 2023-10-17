class Aluno:
    def __init__(self, num_id, nome, turma) -> None:
        self.num_id = num_id
        self.nome = nome
        self.turma = turma
        pass
    def to_string(self):
        return f'numid = {self.num_id}, nome = {self.nome}, turma = {self.turma}'