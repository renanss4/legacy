

class Autor:
    def __init__(self, codigo: int, nome: str):
        assert isinstance(codigo, int) and isinstance(nome, str)

        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
