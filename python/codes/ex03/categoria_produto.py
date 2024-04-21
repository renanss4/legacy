class CategoriaProduto:

    def __init__(self, titulo):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    def __str__(self):
        """Retorna uma representação de string da categoria de produto."""
        return f"Título: {self.titulo}"
