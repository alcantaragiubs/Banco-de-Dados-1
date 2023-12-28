from typing import Optional

from model.users import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()
        
    def create(self, nome=None) -> Optional[User]:
        if(nome is None):
            nome = input('Como você quer se chamar? > ')
            
        newUser = User(nome, 100, "0%", 50, 20, 1, 1)
        
        self.userRepository.saveUser(newUser)
        
        foundUser = self.userRepository.findUserByName(nome)

        return foundUser
    
    def login(self) -> Optional[User]:
        print('Você está de volta! Os seguintes personagens estão disponíveis: \n')
        
        availableUsers = self.userRepository.findAll()
        availableNicknames = []
        
        for user in availableUsers:
            availableNicknames.append(user.nome)
            print(user.nome)
            
        nickname = input('\nDigite o nome do seu usuário: ')
        
        if(nickname not in availableNicknames):
            willCreateNewUser = input("O personagem informado não existe! Deseja cria-lo? (S/n)\n")
            if willCreateNewUser in ['s', 'S']:
                newUser = self.create(nickname)
                # print(newUser)
                return newUser
            else:
                return None
        else:
            return self.userRepository.findUserByName(nickname)
