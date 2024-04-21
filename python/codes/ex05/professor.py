from funcionario import Funcionario

class Professor(Funcionario):

    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, 20)  # Professores têm 20 dias de empréstimo

    def emprestar(self, titulo_livro):
        return f'Professor do departamento "{super().departamento}" pegou emprestado o livro: {titulo_livro} com {super().dias_de_emprestimo} dias de prazo'
        
    def devolver(self, titulo_livro):
        return f'Professor do departamento "{super().departamento}" devolveu o livro: ' + titulo_livro
