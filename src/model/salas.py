class Sala:
    def __init__(self, id, nome, descricao, id_nivel, destinos):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.id_nivel = id_nivel
        self.destinos = destinos
        
    def __str__(self):
        return f"Sala[id={self.id}, nome={self.nome}, descricao={self.descricao}, id_nivel={self.id_nivel}, destinos={self.destinos}]"