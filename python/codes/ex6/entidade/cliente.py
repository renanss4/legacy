from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, codigo: int, nome: str):
        self.__nome = nome
        self.__codigo = codigo

    # Propriedade para obter o nome do cliente
    @property
    def nome(self):
        return self.__nome
    
    # Propriedade para obter o código do cliente
    @property
    def codigo(self):
        return self.__codigo
