from pessoa import Pessoa

class Tecnico(Pessoa):
    def __init__(self, codigo: int, nome: str):
        self.__nome = nome
        self.__codigo = codigo

    # Propriedade para obter o nome do técnico
    @property
    def nome(self):
        return self.__nome
    
    # Propriedade para obter o código do técnico
    @property
    def codigo(self):
        return self.__codigo
