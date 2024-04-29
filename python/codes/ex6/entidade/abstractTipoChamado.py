from abc import ABC, abstractmethod

class AbstractTipoChamado(ABC):
    # Propriedade abstrata para obter o código do tipo de chamado
    @property
    @abstractmethod
    def codigo(self) -> int:
        pass

    # Propriedade abstrata para obter a descrição do tipo de chamado
    @property
    @abstractmethod
    def descricao(self) -> str:
        pass

    # Propriedade abstrata para obter o nome do tipo de chamado
    @property
    @abstractmethod
    def nome(self) -> str:
        pass
