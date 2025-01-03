from abc import abstractmethod
from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU):

    @abstractmethod
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        assert isinstance(departamento, str), "O departamento deve ser uma string"
        self.__departamento = departamento
        
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento: str):
        if isinstance(departamento, str):
            self.__departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro):
        return f'do departamento "{self.__departamento}" pegou emprestado o livro: {titulo_livro} com {super().dias_de_emprestimo} dias de prazo'

    @abstractmethod
    def devolver(self, titulo_livro):
        return f'Funcionario administrativo do departamento {self.__departamento} devolveu o livro: ' + titulo_livro
