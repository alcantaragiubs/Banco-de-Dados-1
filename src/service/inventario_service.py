from typing import Optional

from model.inventario import Inventario
from repositories.inventario_repository import InventarioRepository


class InventarioService:
    def __init__(self):
        self.inventarioRepository = InventarioRepository()
    
    def getInventaryWithItems(self, userId):
        inventary = self.inventarioRepository.findInventaryWithItemsByUserId(userId)

        if(inventary is None):
            print("Inventario está vazio!")

            resp = input('Aperte qualquer tecla para continuar: \n')

            return None
        else:
            print("Você possui os seguinte items: \n")

            print(inventary)

            print('Aperte qualquer tecla para continuar: \n')

            inp = input('> ')
            
        return inventary
    
    def getUserInventary(self, userId):
        inventary = self.inventarioRepository.findInventaryByUserId(userId)
        
        if(inventary is None):
            print("Inventario está vazio!")

            print('Aperte qualquer tecla para continuar: \n')

            inp = input('> ')

            return None

        return inventary
    
