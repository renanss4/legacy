from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__tipo = tipo

    '''
    @return Retorna o tipo do personagem
    '''
    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    '''
    @return Retorna a energia do personagem
    '''
    @property
    def energia(self) -> int:
        return self.__energia

    '''
    @return Retorna a habilidade do personagem
    '''
    @property
    def habilidade(self) -> int:
        return self.__habilidade

    '''
    @return Retorna a velocidade do personagem
    '''
    @property
    def velocidade(self) -> int:
        return self.__velocidade

    '''
    @return Retorna a resistencia do personagem
    '''
    @property
    def resistencia(self) -> int:
        return self.__resistencia
