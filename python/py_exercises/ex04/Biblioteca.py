from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros