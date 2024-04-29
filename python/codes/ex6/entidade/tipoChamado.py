from abstractTipoChamado import AbstractTipoChamado

class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome

    # Propriedade para obter o código do tipo de chamado
    @property
    def codigo(self) -> int:
        return self.__codigo

    # Propriedade para obter a descrição do tipo de chamado
    @property
    def descricao(self) -> str:
        return self.__descricao 

    # Propriedade para obter o nome do tipo de chamado
    @property
    def nome(self) -> str:
        return self.__nome
