from model.npc import NPC
class Inimigo(NPC):
    def __init__(self, nome, fala, id_sala, vida, ataque, id=None):
        super().__init__(nome, fala, id_sala)
        self.id = id
        self.vida = vida
        self.ataque = ataque
        
    def __str__(self):
        return f"Inimigo[id={self.id}, nome={self.nome}, vida={self.vida}, ataque={self.ataque}]"