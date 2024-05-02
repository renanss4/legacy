from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico

class Chamado(AbstractChamado):
    def __init__(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        self.__data = data
        self.__cliente = cliente
        self.__tecnico = tecnico
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tipo = tipo

    # Propriedade para obter o cliente do chamado
    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    # Propriedade para obter a data do chamado
    @property
    def data(self) -> Date:
        return self.__data

    # Propriedade para obter a descrição do chamado
    @property
    def descricao(self) -> str:
        return self.__descricao

    # Propriedade para obter a prioridade do chamado
    @property
    def prioridade(self) -> int:
        return self.__prioridade

    # Propriedade para obter o técnico do chamado
    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico

    # Propriedade para obter o tipo do chamado
    @property
    def tipo(self) -> TipoChamado:
        return self.__tipo

    # Propriedade para obter o título do chamado
    @property
    def titulo(self) -> str:
        return self.__titulo
