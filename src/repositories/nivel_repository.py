from typing import Optional

from database.database_handler import DatabaseHandler
from model.narrador import Narrador


class NarradorRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()

    def updateNarrador(self, user: Narrador) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "UPDATE INTO public.Narrador(fala, id_salar) VALUES(%s, %s)",
                    [user.id_sala, user.id_sala]  
                 )
    
    def deleteNarrador(self, id) -> None:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.Narrador WHERE id = %s",
                    [id]
                )
    
    def findUserById(self, id) -> Optional[Narrador]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                   "SELECT fala, id_salar, id FROM public.Narrador WHERE id = %s",
                    [id]
                )
                result = cursor.fetchone()
    
        if result is None:
            print(f'Narrador com id {id} não encontrado!')
            return None
        
        user = Narrador(*result)
        
        return user
    
    def findAll(self) -> list[Narrador]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                   "SELECT fala, id_salar, id FROM public.Narrador WHERE id = %s",
                    [id]
                     )
                result = cursor.fetchall()
        
        users = [Narrador(*row) for row in result]
        
        return users    