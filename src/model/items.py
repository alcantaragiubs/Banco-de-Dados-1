class Item:
    def __init__(self, nome, descricao, id_inventario, tipo, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.id_inventario = id_inventario
        self.tipo = tipo
        
    def __str__(self):
        return f"Item[id={self.id}, nome={self.nome}, descricao={self.descricao}, id_inventario={self.id_inventario},tipo={self.tipo}]"
