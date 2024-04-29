from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico

class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []  # Inicializa a lista de clientes
        self.__tecnicos = []  # Inicializa a lista de técnicos

    # Propriedade para obter a lista de clientes
    @property
    def clientes(self):
        return self.__clientes

    # Propriedade para obter a lista de técnicos
    @property
    def tecnicos(self):
        return self.__tecnicos

    # Método para incluir um novo cliente na lista de clientes
    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        for cliente_existente in self.__clientes:
            if cliente_existente.codigo == codigo:
                return None  # Já existe um cliente com o mesmo código
        # Se não existe um cliente com o mesmo código, cria um novo e adiciona à lista
        novo_cliente = Cliente(codigo, nome)
        self.__clientes.append(novo_cliente)
        return novo_cliente

    # Método para incluir um novo técnico na lista de técnicos
    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        for tecnico_existente in self.__tecnicos:
            if tecnico_existente.codigo == codigo:
                return None  # Já existe um técnico com o mesmo código
        # Se não existe um técnico com o mesmo código, cria um novo e adiciona à lista
        novo_tecnico = Tecnico(codigo, nome)
        self.__tecnicos.append(novo_tecnico)
        return novo_tecnico
