class Magico:
    def __init__(self, nome, descricao, multi_vida, teletransporte, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.multi_vida = multi_vida
        self.teletransporte = teletransporte

        
    def __str__(self):
        return f"Magico[id={self.id}, nome={self.nome}, descricao={self.descricao}, multi_vida={self.multi_vida}, teletransporte={self.teletransporte}]"
