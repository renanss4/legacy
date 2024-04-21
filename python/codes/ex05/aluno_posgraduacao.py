from aluno import Aluno

class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int, elaborando_tese: bool = True):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = elaborando_tese
        if self.__elaborando_tese:
            self.dias_de_emprestimo *= 2  # Se estiver elaborando tese, o prazo é dobrado

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, value):
        self.__elaborando_tese = value

    def emprestar(self, titulo_livro):
        return f'Aluno de matricula "{super().matricula}" pegou emprestado o livro: {titulo_livro} com {super().dias_de_emprestimo} dias de prazo'
    
    def devolver(self, titulo_livro):
        return f'Aluno de matricula "{super().matricula}" devolveu o livro: ' + titulo_livro
