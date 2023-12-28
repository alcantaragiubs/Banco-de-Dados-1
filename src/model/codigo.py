class Codigo:
    def __init__(self, nome,descricao, multi_ataque, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        
    def __str__(self):
        return f"Codigo[id={self.id}, nome={self.nome}, descricao={self.descricao}]"
