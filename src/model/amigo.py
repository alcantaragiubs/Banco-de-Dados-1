class Amigo:
    def __init__(self, Mult_inventario,id_jogador, id_sala, id=None):
        self.id = id
        self.Mult_inventario = Mult_inventario
        self.id_jogador = id_jogador
        
    def __str__(self):
        return f"Amigo[id={self.id}, Mult_inventario={self.Mult_inventario}, id_jogador={self.id_jogador}]"
