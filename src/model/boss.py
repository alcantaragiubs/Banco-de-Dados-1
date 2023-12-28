from model.inimigo import Inimigo
class Boss(Inimigo):
    def __init__(self, id, nome, fala, id_sala, vida, ataque, multi_vida, multi_ataque, id_nivel):
        super().__init__(nome, fala, id_sala, vida, ataque)
        self.id = id
        self.multi_vida = multi_vida
        self.multi_ataque = multi_ataque
        self.id_nivel = id_nivel
        
    def __str__(self):
        return f"Boss[id={self.id}, multi_vida={self.multi_vida}, multi_ataque={self.multi_ataque}, id_nivel={self.id_nivel}]"
