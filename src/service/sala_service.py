from typing import Optional

from model.salas import Sala
from repositories.sala_repository import SalaRepository
from repositories.user_repository import UserRepository
from repositories.inventario_repository import InventarioRepository

from model.users import User

from model.users import User

class SalaService:
    def __init__(self):
        self.salaRepository = SalaRepository()
        self.userRepository = UserRepository()
        self.inventarioRepository = InventarioRepository()
    
    def getSala(self, user):
        salaAtual = self.salaRepository.salaAtual(user)
        return salaAtual
    
    def mover(self, user: User) -> Optional[User]:
        salaAtual = self.salaRepository.salaAtual(user)
        
        inp = input("Você possui as seguintes opções:\n" +
                "L - Leste: Sala " + str(salaAtual.destinos[0]) + "\n" +
                "O - Oeste: Sala " + str(salaAtual.destinos[1]) + "\n" +
                "N - Norte: Sala " + str(salaAtual.destinos[2]) + "\n" +
                "S - Sul: Sala " + str(salaAtual.destinos[3]) + "\n"
                "Digite sua escolha: ")
        
        if inp == 'l' or inp == 'L':
            self.salaRepository.updateSala(user, salaAtual.destinos[0])
        elif inp == 'o' or inp == 'O':
            self.salaRepository.updateSala(user, salaAtual.destinos[1])
        elif inp == 'n' or inp == 'N':
            self.salaRepository.updateSala(user, salaAtual.destinos[2])
        elif inp == 's' or inp == 'S':
            self.salaRepository.updateSala(user, salaAtual.destinos[3])
        
        result = self.userRepository.findUserByName(user.nome)
        
        if result is not None:
            user = result
        else:
            print('User not found')

        print(user)

        return user
    
    def encontrarBau(self, user: User, inventaryId):
        print('Você encontrou um baú com o seguinte conteúdo:\n')
        bau = self.salaRepository.encontrarBau(user)
        
        print(bau[4] + ": " + bau[5] + "\n")
        print('Deseja adicionar o item ao seu inventário? (s/n):')
        inp = input('> ')

        if(inp == 's' or inp == 'S'):
            self.inventarioRepository.addItemToInvenatary(inventaryId, bau[1])
            print('Item adicionado ao inventário!\n')      
        else:
            print('Item descartado!\n')
       
