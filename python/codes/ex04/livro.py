
from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int,
                 editora: 'Editora', autor: 'Autor',
                 numero_capitulo: int, titulo_capitulo: str):
        # assert -> "afirmar/garantir"
        assert isinstance(codigo, int) and isinstance(titulo, str) \
            and isinstance(ano, int)
        assert isinstance(editora, Editora) \
            and isinstance(autor, Autor)
        assert isinstance(numero_capitulo, int) \
            and isinstance(titulo_capitulo, str)

        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int) -> None:
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self) -> 'Editora':
        return self.__editora

    @editora.setter
    def editora(self, editora: 'Editora') -> None:
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def autores(self) -> list:
        return self.__autores

    def incluir_autor(self, autor: 'Autor') -> None:
        if isinstance(autor, Autor) and autor not in self.__autores \
                and autor is not None:
            self.__autores.append(autor)

    def excluir_autor(self, autor: 'Autor') -> None:
        if isinstance(autor, Autor) and autor in self.__autores \
                and autor is not None:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str) -> None:
        if isinstance(numero, int) and isinstance(titulo, str):
            titulo_nao_existente = True
            for capitulo in self.__capitulos:
                if capitulo.titulo == titulo:
                    titulo_nao_existente = False
                    return
            if titulo_nao_existente:
                self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str) -> None:
        if isinstance(titulo, str):
            # just exercising while also
            '''i = 0
            while i < len(self.__capitulos):
                if self.__capitulos[i].titulo == titulo:
                    del self.__capitulos[i]
                    break
                i += 1'''
            for elemento in self.__capitulos:
                if elemento.titulo == titulo:
                    self.__capitulos.remove(elemento)

    def find_capitulo_by_titulo(self, titulo: str) -> Capitulo:
        if isinstance(titulo, str):
            for capitulo in self.__capitulos:
                if capitulo.titulo == titulo:
                    return capitulo
