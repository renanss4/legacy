from abc import ABC, abstractmethod

class AbstractPessoa(ABC):
    # Método construtor abstrato
    @abstractmethod
    def __init__(self):
        pass

    # Propriedade abstrata para obter o código da pessoa
    @property
    @abstractmethod
    def codigo(self) -> int:
        pass
    
    # Propriedade abstrata para obter o nome da pessoa
    @property
    @abstractmethod
    def nome(self) -> str:
        pass
