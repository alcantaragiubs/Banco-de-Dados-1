from typing import Optional

from database.database_handler import DatabaseHandler
from model.users import User


class UserRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()

    def saveUser(self, user: User) -> None:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO public.Jogador(nome, vida, progresso, ataque, defesa, id_sala, id_nivel) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                    [user.nome, user.vida, user.progresso, user.ataque, user.defesa, user.id_sala, user.id_nivel]
                )

    def updateUser(self, user: User) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE public.Jogador SET nome = %s, vida = %s, progresso = %s, ataque = %s, defesa = %s, id_sala = %s, id_nivel = %s WHERE id = %s",
                    [user.nome, user.vida, user.progresso, user.ataque, user.defesa, user.id_sala, user.id_nivel, user.id]
                )
    
    def deleteUser(self, id) -> None:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.Jogador WHERE id = %s",
                    [id]
                )
    
    def findUserByName(self, nome) -> Optional[User]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT nome, vida, progresso, ataque, defesa, id_sala, id_nivel, id FROM public.Jogador WHERE nome = %s",
                    [nome]
                )
                result = cursor.fetchone()
        
        if result is None:
            print(f'Usuário com nome {nome} não encontrado!')
            return None
        
        user = User(*result)
        
        return user
    
    def findUserById(self, id) -> Optional[User]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT nome, vida, progresso, ataque, defesa, id_sala, id_nivel, id FROM public.Jogador WHERE id = %s",
                    [id]
                )
                result = cursor.fetchone()
    
        if result is None:
            print(f'Usuário com id {id} não encontrado!')
            return None
        
        user = User(*result)
        
        return user
    
    def findAll(self) -> list[User]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT nome, vida, progresso, ataque, defesa, id_sala, id_nivel, id FROM public.Jogador " 
                    )
                result = cursor.fetchall()
        
        users = [User(*row) for row in result]
        
        return users
    
    def updateVida(self, user: User) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE public.Jogador SET vida = %s WHERE id = %s",
                    [user.vida, user.id]
                )