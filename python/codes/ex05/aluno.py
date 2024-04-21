from abc import abstractmethod
from usuario_bu import UsuarioBU

class Aluno(UsuarioBU):

    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        assert isinstance(matricula, int), "A matrícula deve ser um inteiro"
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula

    def emprestar(self, titulo_livro):
        return self.__matricula

    def devolver(self, titulo_livro):
        return f'Aluno de matricula "{self.__matricula}" devolveu o livro: ' + titulo_livro
