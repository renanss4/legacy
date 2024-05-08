from imposto import Imposto


class IPI(Imposto):
    '''
    O calculo da Aliquota do IPI (percentual do imposto) leva em conta
    se existe "aliquota_adicional".
    Se existir aliquota_adicional, a aliquota e aumentada em 10%.
    Por exemplo, se a aliquota informada no construtor for 10.0
    e existe "aliquota_adicional", entao a aliquota calculada sera de 11.0.
    '''
    def __init__(self, aliquota, tem_aliquota_adicional):
        self.__aliquota = aliquota
        self.__tem_aliquota_adicional = tem_aliquota_adicional

    def calcula_aliquota(self):
        if self.__tem_aliquota_adicional:
            aumento = self.__aliquota * 0.1
            valor = self.__aliquota + aumento
            return valor
        return self.__aliquota
