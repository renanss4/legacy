from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa

class Pessoa(AbstractPessoa, ABC):
    # Método construtor abstrato
    @abstractmethod
    def __init__(self, codigo: int, nome: str):
        self.__nome = nome
        self.__codigo = codigo

    # Propriedade para obter o nome da pessoa
    @property
    def nome(self):
        return self.__nome
    
    # Propriedade para obter o código da pessoa
    @property
    def codigo(self):
        return self.__codigo
