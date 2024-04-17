

class Capitulo:
    def __init__(self, numero: int, titulo: str):
        assert isinstance(numero, int) and isinstance(titulo, str)

        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        if isinstance(titulo, str):
            self.__titulo = titulo
