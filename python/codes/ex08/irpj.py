from imposto import Imposto


class IRPJ(Imposto):
    '''
    O calculo da Aliquota do IRPJ (percentual do imposto) leva em conta
    o "desconto".
    O valor de "desconto" deve ser subtraido da aliquota informada.
    Por exemplo, se a aliquota informada no construtor for 10.0
    e o "desconto" for 1, entao a aliquota calculada sera de 9.0
    '''
    def __init__(self, aliquota, desconto):
        self.__aliquota = aliquota
        self.__desconto = desconto

    def calcula_aliquota(self):
        valor = self.__aliquota - self.__desconto
        return valor
