from abc import ABC, abstractmethod
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado
from datetime import date as Date

class AbstractChamado(ABC):
    # Propriedade abstrata para obter o cliente do chamado
    @property
    @abstractmethod
    def cliente(self) -> Cliente:
        pass

    # Propriedade abstrata para obter a data do chamado
    @property
    @abstractmethod
    def data(self) -> Date:
        pass

    # Propriedade abstrata para obter a descrição do chamado
    @property
    @abstractmethod
    def descricao(self) -> str:
        pass

    # Propriedade abstrata para obter a prioridade do chamado
    @property
    @abstractmethod
    def prioridade(self) -> int:
        pass

    # Propriedade abstrata para obter o técnico do chamado
    @property
    @abstractmethod
    def tecnico(self) -> Tecnico:
        pass

    # Propriedade abstrata para obter o tipo do chamado
    @property
    @abstractmethod
    def tipo(self) -> TipoChamado:
        pass

    # Propriedade abstrata para obter o título do chamado
    @property
    @abstractmethod
    def titulo(self) -> str:
        pass
