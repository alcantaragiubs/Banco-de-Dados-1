class Inventario:
    def __init__(self, id, tamanho_inventario, id_jogador):
        self.id = id
        self.tamanho_inventario = tamanho_inventario
        self.id_jogador = id_jogador
        
    def __str__(self):
        return f"Inventario[id={self.id}, tamanho_inventario={self.tamanho_inventario}, id_jogador={self.id_jogador}]"
