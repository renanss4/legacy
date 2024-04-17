
from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: 'Livro') -> None:
        """Add a book to the library."""
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluir_livro(self, livro: 'Livro') -> None:
        """Remove a book from the library."""
        if isinstance(livro, Livro) and livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self) -> list:
        """Return the list of books in the library."""
        return self.__livros
