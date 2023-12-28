class Narrador:
    def __init__(self, fala, id_sala, id=None):
        self.id = id
        self.fala = fala
        self.id_sala = id_sala
        
    def __str__(self):
        return f"Narrador[id={self.id}, fala={self.fala}, id_sala={self.id_sala}]"
