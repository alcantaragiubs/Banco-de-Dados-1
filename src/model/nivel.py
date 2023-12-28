class Nivel:
    def __init__(self, descricao, id=None):
        self.id = id
        self.descricao = descricao
        
    def __str__(self):
        return f"Nivel[id={self.id}, descricao={self.descricao}]"
