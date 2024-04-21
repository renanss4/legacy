from funcionario import Funcionario

class Administrativo(Funcionario):

    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, 10)  # Funcionário administrativo tem 10 dias de empréstimo

    def emprestar(self, titulo_livro):
            return f'Funcionario administrativo do departamento "{super().departamento}" pegou emprestado o livro: {titulo_livro} com {super().dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro):
        return f'Funcionario administrativo do departamento "{super().departamento}" devolveu o livro: ' + titulo_livro
