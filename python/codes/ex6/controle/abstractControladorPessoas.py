from abc import ABC, abstractmethod, abstractproperty
from cliente import Cliente
from tecnico import Tecnico

class AbstractControladorPessoas(ABC):
    # Propriedade abstrata para obter a lista de clientes
    @abstractproperty
    @property
    def clientes(self) -> list:
        pass

    # Propriedade abstrata para obter a lista de técnicos
    @abstractproperty
    @property
    def tecnicos(self) -> list:
        pass

    # Método abstrato para incluir um novo cliente na lista de clientes
    # @param codigo: código do Cliente
    # @param nome: nome do Cliente
    # @return: retorna o cliente inserido
    @abstractmethod
    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        pass

    # Método abstrato para incluir um novo técnico na lista de técnicos
    # @param codigo: código do técnico
    # @param nome: nome do técnico
    # @return: retorna o técnico inserido
    @abstractmethod
    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        pass
