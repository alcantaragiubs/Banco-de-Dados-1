from typing import Optional

from database.database_handler import DatabaseHandler
from model.salas import Sala
from model.inimigo import Inimigo
from model.comum import Comum
from model.boss import Boss
from model.users import User

class SalaRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()
        
    def salaAtual(self, user: User):
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, descricao, id_nivel, destinos FROM public.Sala WHERE id = %s",
                    [user.id_sala]
                        )
                result = cursor.fetchone()

        print(result)
        salaAtual = Sala(*result)
            
        return salaAtual
    
    def updateSala(self, user: User, opcao: int) -> None:
       # assert user.id is not None
        print(user)
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "UPDATE public.Jogador SET id_sala = %s WHERE id = %s ",
                    [opcao, user.id]  
                 )
    
    def findSalaById(self, id) -> Optional[Sala]:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, descricao, id_nivel, destinos FROM public.Sala WHERE id = %s",
                    [id]
                )
                result = cursor.fetchone()
        
        if result is None:
            print(f'Sala com id {id} não encontrada!')
            return None
        
        sala = Sala(*result)
        
        return sala

    def encontrarInimigos(self, user: User):
       # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                        FROM public.comum
                        join public.inimigo on public.comum.id_inimigo = public.inimigo.id
                        join public.npc on public.npc.id_sala = %s and public.inimigo.id_npc=npc.id;
                    """,
                        [user.id_sala])
                result = cursor.fetchone()
        print(result)

        inimigo = Comum(*result)

        return inimigo
    
    def encontrarBau(self, user: User):
        # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * 
                        from Bau
                        join Item on Bau.id_item = Item.id
                        WHERE id_sala = %s
                    """,
                        [user.id_sala])
                bau = cursor.fetchone()
        
        return bau
    