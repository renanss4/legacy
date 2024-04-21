class Produto:

    def __init__(self, codigo=None, descricao=None, categoria_produto=None):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = None

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self.__categoria_produto = categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        """Calcula o preço total do produto."""
        return self.quantidade * self.preco_unitario

    def __str__(self):
        """Retorna uma representação de string do produto."""
        """Tupla = ()"""
        return (
            f"Código: {self.codigo}, "
            f"Descrição: {self.descricao}, "
            f"Categoria: {self.categoria_produto}, "
            f"Quantidade: {self.quantidade}, "
            f"Preço Unitário: {self.preco_unitario}"
        )
