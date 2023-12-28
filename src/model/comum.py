from model.inimigo import Inimigo

class Comum(Inimigo):
    def __init__(self, id, nome, fala, id_sala, vida, ataque):
        super().__init__(nome, fala, id_sala, vida, ataque)
        self.id = id