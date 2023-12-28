class Bau:
    def __init__(self, id_item, id_sala, id=None):
        self.id = id
        self.id_item = id_item
        self.id_sala = id_sala
        
    def __str__(self):
        return f"Bau[id={self.id}, id_item={self.id_item}, id_sala={self.id_sala}]"
