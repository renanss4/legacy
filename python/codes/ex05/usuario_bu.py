from abc import ABC, abstractmethod

class UsuarioBU(ABC):

	@abstractmethod
	def __init__(self, cpf: int, dias_de_emprestimo: int):
		assert isinstance(cpf, int), "O CPF deve ser um inteiro"
		assert isinstance(dias_de_emprestimo, int), "Os dias de empréstimo deve ser um inteiro"
		self.__cpf = cpf
		self.__dias_de_emprestimo = dias_de_emprestimo

	@property
	def cpf(self):
		return self.__cpf
	
	@cpf.setter
	def cpf(self, cpf: str):
		if isinstance(cpf, str):
			self.__cpf = cpf

	@property
	def dias_de_emprestimo(self):
		return self.__dias_de_emprestimo
	
	@dias_de_emprestimo.setter
	def dias_de_emprestimo(self, dias_de_emprestimo: int):
		if isinstance(dias_de_emprestimo, int):
			self.__dias_de_emprestimo = dias_de_emprestimo
			
	def emprestar(self, titulo_livro):
		pass
	
	def devolver(self, titulo_livro):
		pass
