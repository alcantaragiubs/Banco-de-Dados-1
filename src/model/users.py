class User:
    def __init__(self, nome, vida, progresso, ataque, defesa, id_sala, id_nivel, id=None):
        self.id = id
        self.nome = nome
        self.vida = vida
        self.progresso = progresso
        self.ataque = ataque
        self.defesa = defesa
        self.id_sala = id_sala
        self.id_nivel = id_nivel
        
    def __str__(self):
        return f"User[id={self.id}, username={self.nome}, vida={self.vida}, progresso={self.progresso}, ataque={self.ataque}, defesa={self.defesa}, id_sala={self.id_sala}, id_nivel={self.id_nivel}]"
