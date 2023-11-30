class Aluno:
    def __init__(self, id=None, turma=None, nome=None):
        self.id = id
        self.nome = nome
        self.turma = turma
        pass

    def __str__(self):
        return f"Aluno(id={self.id}, turma='{self.turma}', nome='{self.nome}')"
