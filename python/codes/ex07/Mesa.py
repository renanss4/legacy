from AbstractMesa import *
from Carta import *
from Jogador import *


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__cartaJogador1 = cartaJogador1
        self.__cartaJogador2 = cartaJogador2

    '''
    Retorna o Jogador 1
    @return o Jogador 1
    '''
    @property
    def jogador1(self):
        return self.__jogador1

    '''
    Retorna o Jogador 2
    @return o Jogador 2
    '''
    @property
    def jogador2(self):
        return self.__jogador2

    '''
    Retorna a carta que o jogador 1 baixou
    @return carta do jogador 1
    '''
    @property
    def carta_jogador1(self):
        return self.__cartaJogador1

    '''
    Retorna a carta que o jogador 2 baixou
    @return carta do jogador 2
    '''
    @property
    def carta_jogador2(self):
        return self.__cartaJogador2
