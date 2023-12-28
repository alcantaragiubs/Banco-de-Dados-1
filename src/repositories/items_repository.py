from typing import Optional

from database.database_handler import DatabaseHandler
from model.items import Item


class ItemRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()

    def updateItem(self, user: Item) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "UPDATE INTO public.Item(nome, descricao, tipo) VALUES(%s, %s, %s)",
                    [user.nome, user.descricao, user.tipo]  
                 )
    
    def deleteItem(self, id) -> None:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.Jogador WHERE id = %s",
                    [id]
                )
    
    def findUserByName(self, nome) -> Optional[Item]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT nome, descricao, tipo, id FROM public.Item WHERE nome = %s",
                    [nome]
                )
                result = cursor.fetchone()
        
        if result is None:
            print(f'Item com nome {nome} não encontrado!')
            return None
        
        user = Item(*result)
        
        return user
    
    def findUserById(self, id) -> Optional[Item]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                   "SELECT nome, descricao, tipo, id FROM public.Item WHERE nome = %s",
                    [id]
                )
                result = cursor.fetchone()
    
        if result is None:
            print(f'Item com id {id} não encontrado!')
            return None
        
        user = Item(*result)
        
        return user
    
    def findAll(self) -> list[Item]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "SELECT nome, descricao, tipo, id FROM public.Item WHERE nome = %s",
                      )
                result = cursor.fetchall()
        
        users = [Item(*row) for row in result]
        
        return users    