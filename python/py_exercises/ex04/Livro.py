from Editora import Editora
from Autor import Autor
from Capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int,
                 editora: Editora, autor: Autor,
                 numero_capitulo: int, titulo_capitulo: str):
        if isinstance(codigo, int) and isinstance(titulo, str) and \
                isinstance(ano, int):
            self.__codigo = codigo
            self.__titulo = titulo
            self.__ano = ano
        if isinstance(editora, Editora) and isinstance(autor, Autor):
            self.__editora = editora
            self.__autores = [autor]
        if isinstance(numero_capitulo, int) \
                and isinstance(titulo_capitulo, str):
            self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def capitulos(self):
        return self.__capitulos

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and \
                autor not in self.__autores and autor is not None:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and \
                autor in self.__autores and autor is not None:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        if (isinstance(numero, int) and isinstance(titulo, str)):
            for elemento in self.__capitulos:
                if elemento.titulo == titulo:
                    return
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str):
        if isinstance(titulo, str):
            for elemento in self.__capitulos:
                if elemento.titulo == titulo:
                    self.__capitulos.remove(elemento)

    def find_capitulo_by_titulo(self, titulo: str):
        if isinstance(titulo, str):
            for elemento in self.__capitulos:
                if elemento.titulo == titulo:
                    return elemento
