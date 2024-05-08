from imposto import Imposto


class ISS(Imposto):
    '''
    O calculo da Aliquota do ISS (percentual do imposto) leva
    em conta a lista de Servicos
    Para cada servico cadastrado na lista de Servicos do ISS,
    eh reduzido 0,1 da Aliquota.
    Por exemplo, se a aliquota informada no construtor for 10.0 e
    tiverem sido incluidos 2 servicos na lista,
    entao a aliquota calculada sera de 9.8
    '''
    def __init__(self, aliquota):
        self.__aliquota = aliquota
        self.__servicos = []

    def inclui_servico(self, nome: str):
        if nome not in self.__servicos:
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        if nome in self.__servicos:
            self.__servicos.pop(nome)

    def calcula_aliquota(self):
        qtd_servicos = len(self.__servicos)
        if qtd_servicos > 0:
            desconto = qtd_servicos * 0.1
            valor = self.__aliquota - desconto
            return valor
        return self.__aliquota
