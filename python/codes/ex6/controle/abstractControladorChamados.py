from abc import ABC, abstractmethod
from entidade.tipoChamado import TipoChamado
from entidade.chamado import Chamado
from datetime import date as Date
from entidade.cliente import Cliente
from entidade.tecnico import Tecnico

class AbstractControladorChamados(ABC):
    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    @abstractmethod
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        pass

    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um Chamado
    @abstractmethod
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        pass

    # Permite incluir um novo TipoChamado na lista de Tipos de Chamado. O TipoChamado incluido eh retornado como um TipoChamado
    @abstractmethod
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        pass

    # Retorna os tipos de chamado que foram cadastrados no controlador pelo metodo inclui_tipochamado
    @property
    @abstractmethod
    def tipos_chamados(self):
        pass
