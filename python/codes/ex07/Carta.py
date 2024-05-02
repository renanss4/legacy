from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:

        return self.__personagem.energia + \
            self.__personagem.habilidade + \
            self.__personagem.velocidade + \
            self.__personagem.resistencia

    '''
    Retorna para o personagem da carta
    @return personagem da carta
    '''
    @property
    def personagem(self) -> Personagem:
        return self.__personagem
