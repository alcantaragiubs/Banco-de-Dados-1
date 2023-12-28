class Arma:
    def __init__(self, nome,descricao, multi_ataque, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.multi_ataque = multi_ataque
        
    def __str__(self):
        return f"Arma[id={self.id}, nome={self.nome}, descricao={self.descricao}, multi_ataque={self.multi_ataque}]"
