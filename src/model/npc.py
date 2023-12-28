class NPC:
    def __init__(self, nome,fala, id_sala, id=None):
        self.id = id
        self.nome = nome
        self.fala = fala
        self.id_sala = id_sala
        
    def __str__(self):
        return f"NPC[id={self.id}, nome={self.nome}, fala={self.fala}, id_sala={self.id_sala}]"
