# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/doctest.html

from calculadora import soma

# print(soma(1.5, 2.5))
# print(soma(-10, 20))
try:
    print(soma('100', 20))
except AssertionError as e:
    print(f'Conta inválida: {e}')
# try:
#     print(soma('15', 15))
# except TypeError as e:
#     print('Conta inválida: ', e)
