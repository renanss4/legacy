from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict

class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []  # Inicializa a lista de chamados
        self.__tipo_chamados = []  # Inicializa a lista de tipos de chamados
    
    # Método para calcular o total de chamados por tipo
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        total = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                total += 1
        return total

    # Método para incluir um novo chamado na lista de chamados
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(tipo, TipoChamado):
            for chamado_existente in self.__chamados:
                if chamado_existente.data == data and chamado_existente.cliente == cliente and chamado_existente.tecnico == tecnico and chamado_existente.tipo == tipo:
                    return None  # Já existe um chamado com essas características
            # Se não existe um chamado com as mesmas características, cria um novo e adiciona à lista
            novo_chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
            self.__chamados.append(novo_chamado)
            return novo_chamado

    # Método para incluir um novo tipo de chamado na lista de tipos de chamados
    def inclui_tipochamado(self, codigo: int, descricao: str, nome: str) -> TipoChamado:
        for tipo_existente in self.__tipo_chamados:
            if tipo_existente.codigo == codigo:
                return None  # Já existe um tipo de chamado com o mesmo código
        # Se não existe um tipo de chamado com o mesmo código, cria um novo e adiciona à lista
        novo_tipo = TipoChamado(codigo, descricao, nome)
        self.__tipo_chamados.append(novo_tipo)
        return novo_tipo

    # Propriedade para obter a lista de tipos de chamados
    @property	
    def tipos_chamados(self):
        return self.__tipo_chamados
