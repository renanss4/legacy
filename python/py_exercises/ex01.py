"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


"""
    EXERCÍCIO 01: ORDENAÇÃO DE VETOR

    Escreva um programa em Python que receba como entrada uma sequência de números inteiros e imprima os valores recebidos em ordem crescente.

    Siga o exemplo anexo e complete com o seu código.

    Utilize exatamente os mesmos nomes de classe e das operações.

    Gere a String de saída EXATAMENTE como no exemplo.

    Exemplos:

    Vetor de entrada: 4 3 2 1 5
    Saída: "1,2,3,4,5"

    Vetor de entrada: 9 0 5 2 10
    Saída: "0,2,5,9,10"

    IMPORTANTE: Não utilize funções prontas como: array.sort(). Implemente o seu próprio algoritmo de ordenação.
""" 


def to_string(func):
    """
    Decorator that converts the return value of the decorated function to a string,
    removing square brackets for lists and curly braces for dictionaries.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        ValueError: If the return value of the function is not a list or a dictionary.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result_string = ""
            i = 0
            while i < len(result):
                result_string += str(result[i])
                if i < len(result) - 1:
                    result_string += ","
                i += 1
            return result_string
        elif isinstance(result, dict):
            result_string = ""
            values = list(result.values())
            i = 0
            while i < len(values):
                result_string += str(values[i])
                if i < len(values) - 1:
                    result_string += ","
                i += 1
            return result_string
        else:
            raise ValueError("The function did not return a list or a dictionary")
    return wrapper

class Ordenacao():

    def __init__(self, array_para_ordenar:[]): # type: ignore
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar

    @to_string
    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        # Utilizing object-oriented Bubble Sort algorithm as presented by the professor in class
        tamanho = len(self.array_para_ordenar) - 1 # Why? Because  the len function retrieves the size starting from 1, I need it to start from 0, therefore -> -1.
        i = 0
        while i < tamanho:
            # print(f'A -> {self.array_para_ordenar}')
            j = 0
            while j < tamanho - i:
                # print(f'a -> {self.array_para_ordenar}')
                if self.array_para_ordenar[j] > self.array_para_ordenar[j + 1]:
                    temp = self.array_para_ordenar[j]
                    self.array_para_ordenar[j] = self.array_para_ordenar[j + 1]
                    self.array_para_ordenar[j + 1] = temp
                j += 1
            i += 1
        return self.array_para_ordenar

    def to_string(self):
        """
            Converte o conteudo do array em String formatado
            Exemplo: 
            Para o conteudo do array: [1,2,3,4,5]
            Retorna: "1,2,3,4,5"
            @return String com o conteudo do array formatado
        """
        resultado = ""
        i = 0
        tamanho = len(self.array_para_ordenar)
        while i < tamanho:
            resultado += str(self.array_para_ordenar[i])
            # print(i, tamanho-1)
            if i != tamanho - 1:
                resultado += ","
            i += 1
        return resultado
    
a = Ordenacao([2, 4, 5, 4, -2, 0, 1])
print(a.ordena())
# print(a.to_string())