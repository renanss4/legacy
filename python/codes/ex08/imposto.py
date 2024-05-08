from abc import abstractclassmethod, ABC


class Imposto(ABC):
    @abstractclassmethod
    def __init__(self, aliquota):
        self.__aliquota = aliquota

    '''
    Operacao abstrata que ira calcular a aliquota
    Cada classe que ira estender Imposto devera implementar o calculo de acordo
    com a sua regra
    '''
    @abstractclassmethod
    def calcula_aliquota(self) -> float:
        pass

    @property
    def aliquota(self):
        return self.__aliquota
