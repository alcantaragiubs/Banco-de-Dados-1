from database.database_handler import DatabaseHandler
from model.users import User
from model.inimigo import Inimigo
from model.comum import Comum
from model.boss import Boss
class InimigoRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()

    def encontrarInimigos(self, user: User):
        # print(user) 
            
            with self.db.connection as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT *
                            FROM comum
                            where id_sala = %s;
                        """,
                            [user.id_sala])
                    result = cursor.fetchone()
            print(result)

            if result is not None:
                inimigo = Comum(*result)
                return inimigo
            else:
                return None
    
    def encontrarBoss(self, user: User):
       
       # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * 
                        from Boss WHERE id_sala = %s
                    """,
                        [user.id_sala])
                result = cursor.fetchone()
        
        print(result)
        if result is not None:
            boss = Boss(*result)    
            return boss
        else:
            return print('Não há boss nesta sala')